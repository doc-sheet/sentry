from datetime import UTC, datetime, timedelta

from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response

from sentry.api.api_owners import ApiOwner
from sentry.api.api_publish_status import ApiPublishStatus
from sentry.api.base import region_silo_endpoint
from sentry.api.bases.team import TeamEndpoint
from sentry.api.helpers.environments import get_environment_func, get_environments
from sentry.api.serializers import GroupSerializer, serialize
from sentry.models.group import Group, GroupStatus
from sentry.models.team import Team


@region_silo_endpoint
class TeamGroupsOldEndpoint(TeamEndpoint):
    owner = ApiOwner.ISSUES
    publish_status = {
        "GET": ApiPublishStatus.PRIVATE,
    }

    def get(self, request: Request, team: Team) -> Response:
        """
        Return the oldest issues owned by a team
        """
        limit = min(100, int(request.GET.get("limit", 10)))
        environments = [e.id for e in get_environments(request, team.organization)]
        group_environment_filter = (
            Q(groupenvironment__environment_id=environments[0]) if environments else Q()
        )

        group_list = list(
            Group.objects.filter_to_team(team)
            .filter(
                group_environment_filter,
                status=GroupStatus.UNRESOLVED,
                last_seen__gt=datetime.now(UTC) - timedelta(days=90),
            )
            .order_by("first_seen")[:limit]
        )

        return Response(
            serialize(
                group_list,
                request.user,
                GroupSerializer(
                    environment_func=get_environment_func(request, team.organization_id)
                ),
            )
        )
