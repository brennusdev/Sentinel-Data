"""
Identificação das requisições.

O correlation ID permite acompanhar uma operação
através de diferentes componentes do sistema.
"""

from uuid import uuid4


def generate_correlation_id() -> str:
    """
    Gera um identificador único para uma operação.
    """

    return str(
        uuid4()
    )