"""
Consumer Kafka do Sentinel Data.

Responsável por consumir eventos do Kafka
em lotes e encaminhá-los para o pipeline
de processamento.
"""

from kafka import KafkaConsumer

from app.core.config import settings
from processing.pipeline import process_batch


# ============================================================
# KAFKA CONSUMER
# ============================================================

consumer = KafkaConsumer(

    # Tópico que será consumido.
    settings.KAFKA_EVENTS_TOPIC,

    # Endereço dos brokers Kafka.
    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    # Grupo responsável pelo processamento.
    group_id=(
        settings.KAFKA_CONSUMER_GROUP
    ),

    # ========================================================
    # CONTROLE DE BATCH
    # ========================================================
    #
    # O consumer poderá receber até 500
    # registros em uma chamada de poll.
    #
    max_poll_records=500,

    # ========================================================
    # COMMIT MANUAL
    # ========================================================
    #
    # O offset não será confirmado
    # automaticamente.
    #
    enable_auto_commit=False,
)


def consume_messages():
    """
    Consome mensagens do Kafka em lotes.
    """

    while True:

        # ====================================================
        # BUSCA UM LOTE DE MENSAGENS
        # ====================================================

        messages = consumer.poll(

            # Aguarda até 1 segundo
            # por novas mensagens.
            timeout_ms=1000,

            # Limita o tamanho do lote.
            max_records=500,
        )

        # ====================================================
        # PROCESSAMENTO DOS LOTES
        # ====================================================

        for topic_partition, records in (
            messages.items()
        ):

            # Converte as mensagens Kafka
            # em uma lista de eventos Python.
            events = [
                message.value
                for message in records
            ]

            # =================================================
            # PROCESSA O BATCH
            # =================================================

            results = process_batch(
                events
            )

            # =================================================
            # COMMIT DOS OFFSETS
            # =================================================
            #
            # Só confirmamos os offsets depois
            # do processamento do lote.
            #

            consumer.commit()