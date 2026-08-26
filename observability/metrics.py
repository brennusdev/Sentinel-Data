"""
Métricas Prometheus do Sentinel Data.

Este módulo concentra todas as métricas
operacionais da aplicação.
"""

from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Histogram


# ============================================================
# EVENTOS
# ============================================================

EVENTS_RECEIVED = Counter(
    "sentinel_events_received_total",
    "Total de eventos recebidos pelo Sentinel Data",
)


EVENTS_PROCESSED = Counter(
    "sentinel_events_processed_total",
    "Total de eventos processados com sucesso",
)


EVENTS_INVALID = Counter(
    "sentinel_events_invalid_total",
    "Total de eventos considerados inválidos",
)


EVENTS_FAILED = Counter(
    "sentinel_events_failed_total",
    "Total de eventos que falharam durante processamento",
)


# ============================================================
# RETRIES
# ============================================================

EVENT_RETRIES = Counter(
    "sentinel_event_retries_total",
    "Total de tentativas adicionais de processamento",
)


EVENT_DLQ = Counter(
    "sentinel_events_dlq_total",
    "Total de eventos enviados para a Dead Letter Queue",
)


# ============================================================
# LATÊNCIA
# ============================================================

PROCESSING_LATENCY = Histogram(
    "sentinel_processing_latency_seconds",
    "Tempo necessário para processar um evento",
)


# ============================================================
# QUALIDADE
# ============================================================

QUALITY_SCORE = Gauge(
    "sentinel_data_quality_score",
    "Score atual de qualidade dos dados",
)


# ============================================================
# CONSUMER
# ============================================================

CONSUMER_MESSAGES = Counter(
    "sentinel_consumer_messages_total",
    "Mensagens consumidas pelo processor",
)


CONSUMER_ERRORS = Counter(
    "sentinel_consumer_errors_total",
    "Erros encontrados pelo consumer",
)


# ============================================================
# SISTEMA
# ============================================================

ACTIVE_PROCESSORS = Gauge(
    "sentinel_active_processors",
    "Quantidade de processors ativos",
)
# ============================================================
# ESCALABILIDADE — V7
# ============================================================

THROUGHPUT = Gauge(
    "sentinel_events_per_second",
    "Eventos processados por segundo",
)


CONSUMER_LAG = Gauge(
    "sentinel_consumer_lag",
    "Lag atual do consumer",
)