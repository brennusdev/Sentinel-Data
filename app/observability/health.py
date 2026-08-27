"""
Funções auxiliares relacionadas à saúde
da aplicação.
"""

from sqlalchemy import text


def check_database(
    db,
) -> bool:
    """
    Verifica se o PostgreSQL está respondendo.
    """

    try:

        db.execute(
            text("SELECT 1")
        )

        return True

    except Exception:

        return False