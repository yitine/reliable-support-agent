from fastapi import APIRouter

from app.schemas.ask import AskRequest, AskResponse
from app.services.router import route_query

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    route = route_query(request.query)

    return AskResponse(
        answer="",
        confidence=0.0,
        route=route,
        sources=[],
        query=request.query,
    )