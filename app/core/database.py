"""
Configuração da conexão com o banco de dados.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


# Engine responsável pela comunicação
# entre a aplicação e o PostgreSQL.
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)


# Fábrica responsável por criar sessões
# de comunicação com o banco.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """
    Classe base utilizada pelos modelos SQLAlchemy.
    """

    pass


def get_db():
    """
    Cria uma sessão do banco para uma requisição.

    A sessão é encerrada automaticamente após
    o término da requisição.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()