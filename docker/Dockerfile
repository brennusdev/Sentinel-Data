# ============================================================
# BUILD STAGE
# ============================================================

FROM python:3.12-slim AS builder

WORKDIR /build

COPY pyproject.toml .

RUN pip install --upgrade pip


# ============================================================
# RUNTIME STAGE
# ============================================================

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages \
    /usr/local/lib/python3.12/site-packages

COPY app ./app

COPY pyproject.toml .

RUN useradd \
    --create-home \
    --shell /bin/bash \
    sentinel

USER sentinel

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]