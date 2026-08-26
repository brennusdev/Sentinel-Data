# Sentinel Data

# 🛰️ Sentinel Data

> Distributed Event Streaming & Real-Time Data Processing Platform built with Python.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black?logo=apachekafka)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800?logo=grafana)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Sobre o projeto

O **Sentinel Data** é uma plataforma de processamento e observabilidade de dados
orientada a eventos, desenvolvida para estudar e demonstrar conceitos utilizados
na construção de sistemas distribuídos, escaláveis e resilientes.

O projeto foi criado com o objetivo de construir uma arquitetura capaz de:

- receber grandes volumes de eventos;
- processar dados em tempo real;
- processar eventos em batches;
- validar e transformar dados;
- medir qualidade dos dados;
- armazenar informações processadas;
- produzir métricas operacionais;
- detectar falhas;
- realizar retry automático;
- utilizar Dead Letter Queue;
- controlar backpressure;
- trabalhar com múltiplos consumers;
- escalar horizontalmente;
- tolerar falhas de componentes;
- realizar deployments automatizados;
- monitorar a aplicação em produção.

O Sentinel Data não foi desenvolvido apenas como uma API.

Ele foi projetado como um laboratório de engenharia de software para
**Data Engineering, Backend Engineering, Distributed Systems, Observability,
Performance Engineering e DevOps.**

---

# 🎯 Objetivo

O principal objetivo do Sentinel Data é demonstrar como construir uma
plataforma moderna capaz de receber, processar, armazenar e monitorar
eventos em escala.

O fluxo principal da plataforma é:

Client / Producer
        ↓
FastAPI
        ↓
Apache Kafka
        ↓
Consumer Group
        ↓
Batch Processing
        ↓
Data Validation
        ↓
Transformation
        ↓
Data Quality
        ↓
PostgreSQL
        ↓
Analytics
        ↓
Prometheus
        ↓
Grafana

---

# 🧠 Problema que o projeto resolve

Sistemas tradicionais podem começar com uma arquitetura simples:

Client
  ↓
API
  ↓
Database

Esse modelo funciona para aplicações pequenas.

Porém, conforme o volume aumenta, surgem problemas como:

- alto número de requisições simultâneas;
- processamento lento;
- sobrecarga do banco;
- perda de mensagens;
- dificuldade para realizar retry;
- ausência de rastreabilidade;
- dificuldade para identificar gargalos;
- indisponibilidade causada por uma única instância;
- dificuldade para escalar processamento.

O Sentinel Data foi criado para explorar soluções para esses problemas.

---

# 🏗️ Arquitetura

```text
                         CLIENT
                            │
                            ▼
                    ┌───────────────┐
                    │    NGINX      │
                    │ Load Balancer │
                    │ Rate Limiting │
                    └───────┬───────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           API #1         API #2         API #3
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │    KAFKA CLUSTER   │
                 │                    │
                 │ Broker 1           │
                 │ Broker 2           │
                 │ Broker 3           │
                 │                    │
                 │ Replication: 3     │
                 └──────────┬─────────┘
                            │
               ┌────────────┼────────────┐
               ▼            ▼            ▼
           Worker #1    Worker #2    Worker #3
               │            │            │
               └────────────┼────────────┘
                            │
                            ▼
                     Processing Pipeline
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          Validation    Transform      Quality
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                      PostgreSQL
                            │
                            ▼
                        Analytics
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
         Prometheus                   Grafana



