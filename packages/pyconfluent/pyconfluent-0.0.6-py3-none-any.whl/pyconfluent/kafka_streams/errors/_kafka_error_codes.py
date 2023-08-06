from confluent_kafka.cimpl import KafkaError


def _get_invalid_producer_epoch_code():
    """Some versions of confluent-kafka do not support this error code"""
    try:
        return KafkaError.INVALID_PRODUCER_EPOCH
    except AttributeError:
        return 47
