"""
Sentinel Data
---------------
Controle básico de quantidade de requisições.

Observação:
Para produção distribuída, o estado do rate limit
deve ficar em uma solução compartilhada, como Redis.
"""

from time import monotonic

from fastapi import Request
from fastapi import HTTPException
from fastapi import status


# Número máximo de requisições permitidas.
MAX_REQUESTS = 100


# Janela de tempo em segundos.
WINDOW_SECONDS = 60


# Armazena temporariamente os acessos.
_requests = {}


def check_rate_limit(
    request: Request,
) -> None:
    """
    Verifica se o cliente ultrapassou
    o limite de requisições.
    """

    # Obtém o endereço IP.
    client_ip = request.client.host

    # Obtém o tempo atual.
    now = monotonic()

    # Obtém os dados anteriores.
    data = _requests.get(
        client_ip,
        {
            "count": 0,
            "start": now,
        },
    )

    # Verifica se a janela terminou.
    if now - data["start"] >= WINDOW_SECONDS:

        data = {
            "count": 0,
            "start": now,
        }

    # Incrementa a quantidade.
    data["count"] += 1

    # Salva o novo estado.
    _requests[client_ip] = data

    # Bloqueia caso o limite tenha sido ultrapassado.
    if data["count"] > MAX_REQUESTS:

        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded",
        )