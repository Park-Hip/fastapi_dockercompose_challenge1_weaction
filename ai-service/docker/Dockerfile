# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

# Law #8: Do not run as root. 
# -m: Creates a home folder.
# -r: Makes it a "system" user.
# -U: Automatically creates a group named aiuser.
RUN useradd -m -r -U aiuser

# Copy virtual environment from builder
COPY --from=builder --chown=aiuser:aiuser /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY --chown=aiuser:aiuser ./app /app/app

# Switch to the non-privileged user
USER aiuser

# Expose FastAPI port
EXPOSE 8000

# Start command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
