import logging
from enum import StrEnum

from sentry import options


class EventType(StrEnum):
    TRANSACTION = "transaction"
    ERROR = "error"


class TransactionStageStatus(StrEnum):
    # the transaction is stored to rc-transactions
    REDIS_PUT = "redis_put"

    # a save_transactions task is kicked off
    SAVE_TRX_STARTED = "save_trx_started"

    # a save_transactions task is finished
    SAVE_TRX_FINISHED = "save_trx_finished"

    # the transaction is published to the `events` topic for snuba/sbc consumers to consume
    SNUBA_TOPIC_PUT = "snuba_topic_put"

    # the transaction is published to the `snuba-commit-log` topic
    COMMIT_LOG_TOPIC_PUT = "commit_log_topic_put"

    # a post_process task is kicked off
    POST_PROCESS_STARTED = "post_process_started"

    # the transaction is deleted from rc-transactions
    REDIS_DELETED = "redis_deleted"


logger = logging.getLogger("EventTracker")


def track_sampled_event(event_id: str, event_type: str, status: TransactionStageStatus) -> None:
    """
    Records how far an event has made it through the ingestion pipeline.
    Each event type will pick up its sampling rate from its registered option.
    """

    sample_rate = options.get(f"performance.event-tracker.sample-rate.{event_type}")
    if sample_rate == 0:
        return

    event_float = (int(event_id, 16) % 10000) / 10000
    if event_float < sample_rate:
        extra = {
            "event_id": event_id,
            "event_type": getattr(EventType, event_type.upper(), None),
            "status": status,
        }
        _do_record(extra)


def _do_record(extra):
    # All Python logs will be picked up by Google Cloud Logging.
    # TODO: make a google Cloud Sink to filter for these EventTracker logs and put them into BigQuery and do data analysis downstream
    logger.info("EventTracker.recorded", extra=extra)
