from pydantic import BaseModel, Field
from typing import Optional


class AskRequest(BaseModel):
    """Request schema for /ask endpoint"""
    query: str = Field(..., description="User's question or query")
    user_profile: Optional[dict] = Field(
        default=None,
        description="Optional user context (e.g., plan, history)"
    )


class SourceReference(BaseModel):
    """Reference to a source document"""
    id: int
    title: str
    score: float = Field(..., description="Relevance score")


class AskResponse(BaseModel):
    """Response schema for /ask endpoint"""
    answer: str
    confidence: float = Field(..., ge=0, le=1, description="Confidence score 0-1")
    route: str = Field(..., description="Source selected to answer the query: knowledge_base, huggingface, or unknown")
    sources: list[SourceReference] = Field(default_factory=list)
    query: str = Field(..., description="Original query for reference")