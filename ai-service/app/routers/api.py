from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db, engine
from app.models.schemas import SummarizeRequest, SummarizeResponse
from app.services.core import summarize_document, save_summary_history, get_history_records, OLLAMA_MODEL
from typing import List

router = APIRouter()

@router.get("/health", summary="Health Check")
async def health_check():
    # Verify DB connectivity
    try:
        with engine.connect():
            db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {
        "status": "ok",
        "api": "healthy",
        "database": db_status
    }

@router.post("/summarize", response_model=SummarizeResponse, summary="Summarize Document")
async def summarize(request: SummarizeRequest, db: Session = Depends(get_db)):
    try:
        # 1. Ask Ollama to summarize
        summary = await summarize_document(text=request.text)
        
        # 2. Save history in Postgres
        record = save_summary_history(
            db=db,
            original_text=request.text,
            summary=summary,
            model_used=OLLAMA_MODEL
        )
        return record
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[SummarizeResponse], summary="Get History")
async def get_history(limit: int = 10, db: Session = Depends(get_db)):
    records = get_history_records(db=db, limit=limit)
    return records
