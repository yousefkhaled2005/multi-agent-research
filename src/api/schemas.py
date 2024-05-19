from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class ResearchRequest(BaseModel):
    topic: str = Field(..., example="Recent advances in Arabic LLM alignment")
    language: str = Field("ar", example="ar")


class ResearchResponse(BaseModel):
    topic: str
    status: str
    revision_count: int
    sources_count: int
    fact_check_notes: List[str]
    final_report: Optional[str]
