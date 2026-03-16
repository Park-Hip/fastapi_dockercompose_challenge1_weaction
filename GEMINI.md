# Project Role & Mission
You are an expert AI Engineer building a production-grade Document Summarizer API. Your goal is to deliver clean, scalable, and containerized code that avoids common junior developer pitfalls.

# 🚫 The 8 Production "Laws" (Must Avoid)
1. **Base Image:** Use `python:3.11-slim` only. Avoid `python:latest` or heavy images.
2. **Docker Context:** Maintain a strict `.dockerignore`. Do not include `.git`, `__pycache__`, or `.venv`.
3. **Secrets:** NEVER hardcode credentials. Use `os.getenv()` and inject via `docker-compose.yml`.
4. **Race Conditions:** Use Docker `healthcheck` (pg_isready). The API must wait for the DB to be healthy.
5. **Architecture:** No Monoliths. Follow the structure: `app/routers/`, `app/models/`, `app/services/`.
6. **Validation:** Use Pydantic `BaseModel` for all Request/Response schemas. No raw dicts.
7. **CORS:** Do not use `allow_origins=["*"]`. Restricted to `http://localhost:3000` for dev.
8. **Security:** Do not run as `root`. Create a non-privileged user (e.g., `aiuser`) in the Dockerfile.

# Technical Stack
- **Backend:** FastAPI, Uvicorn
- **Database:** PostgreSQL (for history tracking)
- **Validation:** Pydantic v2
- **Containerization:** Docker Compose (Multi-stage build)
- **AI Engine:** Ollama (Local CPU inference)

# Standard Commands
- Build: `docker-compose up --build`
- Test: `pytest`
- Lint: `ruff check .`

# 📁 Required Directory Structure
ai-service/
├── app/                  # All FastAPI code
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── routers/          # API endpoints
│   ├── models/           # Pydantic schemas
│   └── services/         # Business logic/Ollama calls
├── docker/               # Container config
│   ├── Dockerfile
│   └── docker-compose.yml
├── utils/                # Evidence/Screenshots
├── requirements.txt
├── .dockerignore
└── AVOIDANCE_TABLE.md    # Pitfall proof