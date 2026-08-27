"""
Sentinel Data
============================================================

Ponto de entrada principal da aplicação FastAPI.

Responsabilidades deste arquivo:

1. Criar a aplicação FastAPI.
2. Configurar informações básicas da API.
3. Registrar middlewares.
4. Registrar as rotas da aplicação.

IMPORTANTE:
O main.py NÃO deve conter regras de negócio.

Regras de negócio devem ficar em:
    app/services/

Processamento de eventos:
    app/processors/

Kafka:
    app/consumers/

Segurança:
    app/security/

Métricas:
    app/observability/
"""

from fastapi import FastAPI

# Middleware responsável por adicionar
# headers HTTP relacionados à segurança.
from app.middleware.security import (
    SecurityHeadersMiddleware,
)

# Middleware responsável por criar um
# identificador único para cada requisição.
from app.middleware.request_id import (
    RequestIDMiddleware,
)

# Rotas da aplicação.
#
# Caso seus arquivos de rotas ainda não existam,
# vamos criá-los nas próximas etapas.
from app.api.routes import (
    health,
    events,
)


# ============================================================
# CONFIGURAÇÃO DA APLICAÇÃO
# ============================================================

app = FastAPI(
    title="Sentinel Data",
    description=(
        "Plataforma de processamento, "
        "observabilidade e análise de eventos."
    ),
    version="10.0.0",
)


# ============================================================
# MIDDLEWARES
# ============================================================

# ------------------------------------------------------------
# Request ID
# ------------------------------------------------------------
#
# Cada requisição recebe um identificador único.
#
# Exemplo:
#
# Request
#    ↓
# X-Request-ID: 550e8400-e29b-41d4...
#
# Esse identificador pode ser utilizado posteriormente
# para rastrear uma requisição através de:
#
# API → Kafka → Consumer → Processor → Database → Logs
#
app.add_middleware(
    RequestIDMiddleware
)


# ------------------------------------------------------------
# Security Headers
# ------------------------------------------------------------
#
# Adiciona headers HTTP relacionados à segurança.
#
# Exemplos:
#
# X-Content-Type-Options
# X-Frame-Options
# Referrer-Policy
#
app.add_middleware(
    SecurityHeadersMiddleware
)


# ============================================================
# ROTAS
# ============================================================

# ------------------------------------------------------------
# Health Check
# ------------------------------------------------------------
#
# Permite verificar se a API está funcionando.
#
# Exemplo:
#
# GET /health
#
app.include_router(
    health.router
)


# ------------------------------------------------------------
# Event API
# ------------------------------------------------------------
#
# Responsável pelos endpoints relacionados aos eventos
# processados pelo Sentinel Data.
#
# Exemplos futuros:
#
# GET    /events
# GET    /events/{event_id}
# POST   /events
#
app.include_router(
    events.router
)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get(
    "/",
    tags=["System"],
)
async def root():
    """
    Endpoint inicial da aplicação.

    Serve principalmente para verificar rapidamente
    se a API está respondendo.
    """

    return {
        "application": "Sentinel Data",
        "version": "10.0.0",
        "status": "online",
    }