from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Histogram


CIRCUIT_BREAKER_OPEN = Gauge(
    "sentinel_circuit_breaker_open",
    "Estado do circuit breaker",
)


RATE_LIMITED_REQUESTS = Counter(
    "sentinel_rate_limited_requests_total",
    "Requests bloqueadas pelo rate limiter",
)


GRACEFUL_SHUTDOWNS = Counter(
    "sentinel_graceful_shutdowns_total",
    "Quantidade de encerramentos controlados",
)


BATCH_SIZE = Histogram(
    "sentinel_processing_batch_size",
    "Quantidade de eventos processados por lote",
)


RECOVERY_EVENTS = Counter(
    "sentinel_recovery_events_total",
    "Eventos de recuperação do sistema",
)