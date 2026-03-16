# 🛡️ Anti-Junior Pitfall Proof (Avoidance Table)

| Law # | Pitfall | How We Avoided It | Evidence Location / Verification |
|-------|---------|-------------------|----------------------------------|
| 1 | `python:latest` or heavy image | Used `python:3.11-slim` in Dockerfile. | `docker/Dockerfile` |
| 2 | Bloated Docker Context | Added strict `.dockerignore` for `.git`, `.venv`, `__pycache__`. | `.dockerignore` |
| 3 | Hardcoded Secrets | Used `os.getenv()` and injected variables via `docker-compose.yml`. | Code & `docker/docker-compose.yml` |
| 4 | DB Race Conditions | Added `pg_isready` healthcheck in `docker-compose.yml` + `depends_on`. | `docker/docker-compose.yml` |
| 5 | Monolithic Architecture | Strict segregation: `routers/`, `models/`, `services/`. | Entire `app/` hierarchy |
| 6 | Weak Validation / Raw Dicts | Used strictly typed Pydantic V2 `BaseModel` classes. | `app/models/schemas.py` |
| 7 | Wildcard CORS (`*`) | Restricted to `http://localhost:3000` via FastAPI middleware. | `app/main.py` |
| 8 | Running as Root | Created and switched to non-privileged user `aiuser` inside Docker. | `docker/Dockerfile` |
