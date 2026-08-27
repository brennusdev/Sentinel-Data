"""
Sentinel Data
---------------
Middleware responsável por adicionar
headers de segurança às respostas HTTP.
"""

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


class SecurityHeadersMiddleware(
    BaseHTTPMiddleware
):
    """
    Adiciona headers HTTP relacionados
    à segurança.
    """

    async def dispatch(
        self,
        request,
        call_next,
    ):

        # Encaminha a requisição para
        # o próximo componente da aplicação.
        response = await call_next(
            request
        )

        # Impede que o navegador interprete
        # incorretamente o Content-Type.
        response.headers[
            "X-Content-Type-Options"
        ] = "nosniff"

        # Impede que a aplicação seja
        # carregada dentro de um iframe.
        response.headers[
            "X-Frame-Options"
        ] = "DENY"

        # Controla informações enviadas
        # através do header Referer.
        response.headers[
            "Referrer-Policy"
        ] = (
            "strict-origin-when-cross-origin"
        )

        return response