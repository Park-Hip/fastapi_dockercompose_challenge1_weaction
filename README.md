# 🤖 Local Document Summarizer API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_CPU-black?style=for-the-badge&logo=ollama)](https://ollama.com/)

A production-grade, containerized API for text summarization. Built with **FastAPI**, **PostgreSQL** for history tracking, and **Ollama** for local CPU-based inference.

---

## 🚀 Quick Start

### 1. Prerequisites
*   **Docker Desktop** (with Compose)
*   **Ollama** (running on your host machine)
*   Pull the required model:
    ```bash
    ollama pull qwen2.5:1.5b
    ```

### 2. Launch the Service
Navigate to the `ai-service` directory and run:
```bash
docker compose -f docker/docker-compose.yml up --build
```
The API will be available at `http://localhost:8000`.

### 3. API Documentation
Once running, explore the interactive documentation:
*   **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
*   **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠️ Architecture & Tech Stack

Following the **8 Production Laws** defined in `GEMINI.md`, this project is architected for scalability and security:

*   **Backend:** FastAPI (Python 3.11-slim)
*   **Database:** PostgreSQL 15 (History tracking)
*   **ORM:** SQLAlchemy 2.0
*   **Validation:** Pydantic V2
*   **Containerization:** Multi-stage Docker builds (non-root execution)

### 📁 Directory Structure
```text
ai-service/
├── app/                  # FastAPI logic
│   ├── routers/          # API endpoints (/health, /summarize, /history)
│   ├── models/           # Pydantic schemas & SQLAlchemy models
│   └── services/         # Business logic & Ollama integration
├── docker/               # Container config (Dockerfile, Compose)
├── .dockerignore         # Strict context context filtering
└── requirements.txt      # Dependency manifest
```

---

## 🛡️ Production Compliance (The 8 Laws)
This project strictly avoids "junior developer" pitfalls by implementing:
1.  **python:3.11-slim** base images.
2.  **Strict .dockerignore** to prevent context bloat.
3.  **No hardcoded secrets** (injected via Compose).
4.  **DB Healthchecks** (API waits for Postgres to be `healthy`).
5.  **Modular Service-Router architecture**.
6.  **Pydantic BaseModel** for all requests/responses.
7.  **Strict CORS** restricted to `localhost:3000`.
8.  **Non-privileged user (`aiuser`)** inside Docker.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Connectivity check for API and Database. |
| `POST` | `/summarize` | Send text to Ollama for summarization and store in history. |
| `GET` | `/history` | Retrieve the last 10 summarization results. |

---

## 📄 License
MIT License. Created by [Park-Hip](https://github.com/Park-Hip).
