"""
Consumer principal do Sentinel Data.
"""

from app.core.database import SessionLocal
from repositories.event_repository import get_event
from streaming.consumer import create_consumer


def process_message(
    message,
):
    """
    Processa uma mensagem recebida do Kafka.
    """

    payload = message.value

    event_id = payload["id"]

    db = SessionLocal()

    try:
        event = get_event(
            db=db,
            event_id=event_id,
        )

        if event is None:
            print(
                f"Evento {event_id} não encontrado."
            )

            return

        print(
            f"Processando evento {event_id}: "
            f"{event.event_type}"
        )

        # Aqui futuramente entra o pipeline
        # de transformação dos dados.

    finally:
        db.close()


def run_consumer():
    """
    Mantém o consumidor executando continuamente.
    """

    consumer = create_consumer()

    print(
        "Sentinel Data Consumer iniciado."
    )

    try:

        for message in consumer:

            try:

                process_message(message)

                # Confirma que a mensagem foi processada.
                consumer.commit()

            except Exception as error:

                print(
                    f"Erro ao processar mensagem: {error}"
                )

    finally:

        consumer.close()


if __name__ == "__main__":
    run_consumer()