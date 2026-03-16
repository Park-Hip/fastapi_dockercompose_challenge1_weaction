import os
import httpx
from sqlalchemy.orm import Session
from app.models.database import SummaryHistory

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://host.docker.internal:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

async def summarize_document(text: str) -> str:
    prompt = f"Summarize the following text concisely. Only return the summary.\n\nText:\n{text}"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(OLLAMA_API_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()
        except httpx.HTTPError as e:
            raise RuntimeError(f"Failed to communicate with Ollama: {str(e)}")

def save_summary_history(db: Session, original_text: str, summary: str, model_used: str) -> SummaryHistory:
    history_record = SummaryHistory(
        original_text=original_text,
        summary=summary,
        model_used=model_used
    )
    db.add(history_record)
    db.commit()
    db.refresh(history_record)
    return history_record

def get_history_records(db: Session, limit: int = 100):
    return db.query(SummaryHistory).order_by(SummaryHistory.id.desc()).limit(limit).all()
