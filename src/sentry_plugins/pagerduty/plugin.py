from sentry.integrations.base import FeatureDescription, IntegrationFeatures
from sentry.plugins.bases.notify import NotificationPlugin
from sentry.utils.http import absolute_uri
from sentry_plugins.base import CorePluginMixin
from sentry_plugins.utils import get_secret_field_config

from .client import PagerDutyPluginClient


class PagerDutyPlugin(CorePluginMixin, NotificationPlugin):
    description = "Send alerts to PagerDuty."
    slug = "pagerduty"
    title = "PagerDuty"
    conf_key = slug
    conf_title = title
    required_field = "service_key"
    feature_descriptions = [
        FeatureDescription(
            """
            Manage incidents and outages by sending Sentry notifications to PagerDuty.
            """,
            IntegrationFeatures.INCIDENT_MANAGEMENT,
        ),
        FeatureDescription(
            """
            Configure rule based PagerDuty alerts to automatically be triggered in a specific
            service - or in multiple services!
            """,
            IntegrationFeatures.ALERT_RULE,
        ),
    ]

    def error_message_from_json(self, data):
        message = data.get("message", "unknown error")
        errors = data.get("errors", None)
        if errors:
            return "{}: {}".format(message, " ".join(errors))

        return message

    def is_configured(self, project) -> bool:
        return bool(self.get_option("service_key", project))

    def get_config(self, project, user=None, initial=None, add_additional_fields: bool = False):
        service_key = self.get_option("service_key", project)
        secret_field = get_secret_field_config(
            service_key, "PagerDuty's Sentry service Integration Key", include_prefix=True
        )
        secret_field.update({"name": "service_key", "label": "Service Key"})
        return [
            secret_field,
            {
                "name": "routes",
                "label": "Tag routing",
                "type": "textarea",
                "placeholder": "environment,production,KEY1\ndevice,Other,KEY2",
                "required": False,
                "help": (
                    "Route each event to a different PagerDuty service key based "
                    "on the event's tags. Each line should contain a tag, "
                    "value, and service key separated by commas. The first "
                    "line that matches a tag's key and value will send to that "
                    "integration key instead of the main service key above."
                ),
            },
        ]

    def notify_users(self, group, event, triggering_rules) -> None:
        if not self.is_configured(group.project):
            return

        # TODO: This should eventually just be event.title in line with other plugins.
        # However, we should notify users first, since PD alert routing may be
        # based off the message field. We default to the title now because it's
        # possible for `event.message` to be "" and the description
        # is a required field for the PD payload.
        description = (event.message or event.title)[:1024]

        tags = dict(event.tags)
        details = {
            "event_id": event.event_id,
            "project": group.project.name,
            "release": event.get_tag("sentry:release"),
            "platform": event.platform,
            "culprit": event.culprit,
            "datetime": event.datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "tags": tags,
            "url": group.get_absolute_url(params={"referrer": "pagerduty_plugin"}),
        }

        service_key = self.get_option("service_key", group.project)

        routes = self.get_option("routes", group.project) or ""
        for route in (r.strip() for r in routes.split("\n")):
            fields = [f.strip() for f in route.split(",")]
            if len(fields) != 3:
                continue
            tag_key, tag_value, route_service_key = fields
            if tag_key in tags and tags[tag_key] == tag_value:
                service_key = route_service_key
                break

        client = PagerDutyPluginClient(service_key=service_key)
        try:
            response = client.trigger_incident(
                description=description,
                event_type="trigger",
                incident_key=str(group.id),
                details=details,
                contexts=[
                    {
                        "type": "link",
                        "href": absolute_uri(
                            group.get_absolute_url(params={"referrer": "pagerduty_plugin"})
                        ),
                        "text": "View Sentry Issue Details",
                    }
                ],
            )
            assert response["status"] == "success"
        except Exception as e:
            self.raise_error(e)
