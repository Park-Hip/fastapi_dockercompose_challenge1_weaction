from pydantic import BaseModel, Field, ConfigDict

# Law #6: Strict validation using Pydantic V2 BaseModel
class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, description="The original text to be summarized.")

class SummarizeResponse(BaseModel):
    id: int
    original_text: str
    summary: str
    model_used: str

    model_config = ConfigDict(from_attributes=True)
