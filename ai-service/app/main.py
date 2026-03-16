from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.api import router 
from app.models.database import init_db

# Initialize database schemas based on SQLAlchemy metadata
init_db()

app = FastAPI(
    title="Local Document Summarizer API",
    description="Production-grade API for text summarization via host-based local Ollama.",
    version="1.0.0"
)

# Law #7: Strict CORS Policy. No wildcard origins.
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
