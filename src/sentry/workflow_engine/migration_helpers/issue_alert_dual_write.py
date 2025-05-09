import logging
from typing import Any

from sentry.models.rule import Rule
from sentry.rules.conditions.event_frequency import EventUniqueUserFrequencyConditionWithConditions
from sentry.rules.processing.processor import split_conditions_and_filters
from sentry.workflow_engine.migration_helpers.issue_alert_conditions import (
    create_event_unique_user_frequency_condition_with_conditions,
    translate_to_data_condition,
)
from sentry.workflow_engine.migration_helpers.rule_action import (
    build_notification_actions_from_rule_data_actions,
)
from sentry.workflow_engine.models import (
    Action,
    AlertRuleWorkflow,
    DataCondition,
    DataConditionGroup,
    DataConditionGroupAction,
    Workflow,
    WorkflowDataConditionGroup,
)
from sentry.workflow_engine.models.data_condition import Condition
from sentry.workflow_engine.processors.workflow import (
    WorkflowDataConditionGroupType,
    delete_workflow,
)

logger = logging.getLogger(__name__)

SKIPPED_CONDITIONS = [Condition.EVERY_EVENT]


def bulk_create_data_conditions(
    conditions: list[dict[str, Any]],
    dcg: DataConditionGroup,
    filters: list[dict[str, Any]] | None = None,
):
    dcg_conditions: list[DataCondition] = []

    for condition in conditions:
        if condition["id"] == EventUniqueUserFrequencyConditionWithConditions.id:  # special case
            dcg_conditions = [
                create_event_unique_user_frequency_condition_with_conditions(
                    dict(condition), dcg, filters
                )
            ]
        else:
            dcg_conditions.append(translate_to_data_condition(dict(condition), dcg=dcg))

    filtered_data_conditions = [dc for dc in dcg_conditions if dc.type not in SKIPPED_CONDITIONS]

    # try one by one, keeping errors
    for dc in filtered_data_conditions:
        dc.save()


def create_if_dcg(
    workflow: Workflow,
    conditions: list[dict[str, Any]],
    filters: list[dict[str, Any]],
    filter_match: str | None = None,
):
    if filter_match == "any":  # must create IF DCG even if it's empty, to attach actions
        filter_match = DataConditionGroup.Type.ANY_SHORT_CIRCUIT.value
    elif filter_match is None:
        filter_match = DataConditionGroup.Type.ALL.value

    if_dcg = DataConditionGroup.objects.create(
        logic_type=filter_match, organization=workflow.organization
    )
    WorkflowDataConditionGroup.objects.create(workflow=workflow, condition_group=if_dcg)

    conditions_ids = [condition["id"] for condition in conditions]
    # skip migrating filters for special case
    if EventUniqueUserFrequencyConditionWithConditions.id not in conditions_ids:
        bulk_create_data_conditions(conditions=filters, dcg=if_dcg)

    return if_dcg


def create_workflow_actions(if_dcg: DataConditionGroup, actions: list[dict[str, Any]]) -> None:
    notification_actions = build_notification_actions_from_rule_data_actions(actions)
    dcg_actions = [
        DataConditionGroupAction(action=action, condition_group=if_dcg)
        for action in notification_actions
    ]
    DataConditionGroupAction.objects.bulk_create(dcg_actions)


def update_migrated_issue_alert(rule: Rule) -> Workflow | None:
    data = rule.data

    try:
        alert_rule_workflow = AlertRuleWorkflow.objects.get(rule_id=rule.id)
    except AlertRuleWorkflow.DoesNotExist:
        # OK state, rule may not have been migrated
        logger.info(
            "rule was not dual written or objects were already deleted, returning early",
            extra={"rule_id": rule.id},
        )
        return None

    workflow: Workflow = alert_rule_workflow.workflow
    if not workflow.when_condition_group:
        raise Exception("Workflow does not have a when_condition_group")

    conditions, filters = split_conditions_and_filters(data["conditions"])

    update_dcg(
        dcg=workflow.when_condition_group,
        type=WorkflowDataConditionGroupType.WORKFLOW_TRIGGER,
        conditions=conditions,
        filters=filters,
        match=data["action_match"],
    )

    try:
        if_dcg = WorkflowDataConditionGroup.objects.get(workflow=workflow).condition_group
    except WorkflowDataConditionGroup.DoesNotExist:
        # OK state because we can recreate the IF DCG but should not happen
        logger.info(
            "IF DCG for workflow does not exist, recreating",
            extra={
                "workflow_id": workflow.id,
            },
        )
        # if no IF DCG exists, create one
        if_dcg = create_if_dcg(
            workflow=workflow,
            conditions=conditions,
            filters=filters,
            filter_match=data["filter_match"],
        )
        WorkflowDataConditionGroup.objects.create(workflow=workflow, condition_group=if_dcg)

    update_dcg(
        dcg=if_dcg,
        type=WorkflowDataConditionGroupType.ACTION_FILTER,
        conditions=conditions,
        match=data["filter_match"],
        filters=filters,
    )

    delete_workflow_actions(if_dcg=if_dcg)
    create_workflow_actions(if_dcg=if_dcg, actions=data["actions"])  # action(s) must exist

    workflow.environment_id = rule.environment_id
    if frequency := data["frequency"]:
        workflow.config["frequency"] = frequency

    workflow.owner_user_id = rule.owner_user_id
    workflow.owner_team_id = rule.owner_team_id

    workflow.name = rule.label

    workflow.enabled = True
    workflow.save()

    return workflow


def update_dcg(
    dcg: DataConditionGroup,
    conditions: list[dict[str, Any]],
    type: WorkflowDataConditionGroupType,
    filters: list[dict[str, Any]],
    match: str | None = None,
):
    DataCondition.objects.filter(condition_group=dcg).delete()

    if dcg.logic_type != match:
        if match == "any":
            match = DataConditionGroup.Type.ANY_SHORT_CIRCUIT.value
        elif match is None:
            match = DataConditionGroup.Type.ALL.value

        dcg.update(logic_type=match)

    if type == WorkflowDataConditionGroupType.ACTION_FILTER:
        conditions_ids = [condition["id"] for condition in conditions]
        # skip migrating filters for special case
        if EventUniqueUserFrequencyConditionWithConditions.id not in conditions_ids:
            bulk_create_data_conditions(conditions=filters, dcg=dcg)
    else:
        bulk_create_data_conditions(conditions=conditions, filters=filters, dcg=dcg)

    return dcg


def delete_migrated_issue_alert(rule: Rule) -> int | None:
    try:
        alert_rule_workflow = AlertRuleWorkflow.objects.get(rule_id=rule.id)
    except AlertRuleWorkflow.DoesNotExist:
        # OK state, rule may not have been migrated
        logger.info(
            "rule was not dual written or objects were already deleted, returning early",
            extra={"rule_id": rule.id},
        )
        return None

    workflow: Workflow = alert_rule_workflow.workflow
    workflow_id = workflow.id

    delete_workflow(workflow)
    alert_rule_workflow.delete()

    return workflow_id


def delete_workflow_actions(if_dcg: DataConditionGroup):
    dcg_actions = DataConditionGroupAction.objects.filter(condition_group=if_dcg)
    action_ids = dcg_actions.values_list("action_id", flat=True)
    Action.objects.filter(id__in=action_ids).delete()
    dcg_actions.delete()
