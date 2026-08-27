"""
Sentinel Data
---------------
Gera um identificador único para cada requisição.
"""

from uuid import uuid4

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


class RequestIDMiddleware(
    BaseHTTPMiddleware
):
    """
    Adiciona um identificador único
    a cada requisição.
    """

    async def dispatch(
        self,
        request,
        call_next,
    ):

        # Cria um UUID único.
        request_id = str(uuid4())

        # Armazena o ID no estado da requisição.
        request.state.request_id = (
            request_id
        )

        # Continua o processamento.
        response = await call_next(
            request
        )

        # Devolve o ID ao cliente.
        response.headers[
            "X-Request-ID"
        ] = request_id

        return response