"""
Configuração dos tópicos Kafka.
"""

TOPICS = {
    "events.raw": {
        "partitions": 8,
        "replication_factor": 1,
    },

    "events.processed": {
        "partitions": 8,
        "replication_factor": 1,
    },

    "events.invalid": {
        "partitions": 4,
        "replication_factor": 1,
    },

    "events.dlq": {
        "partitions": 4,
        "replication_factor": 1,
    },
}