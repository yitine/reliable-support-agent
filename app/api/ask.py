from fastapi import APIRouter

from app.schemas.ask import AskRequest, AskResponse
from app.services.router import route_query
from app.services.knowledge_base import search_kb
from app.services.huggingface import search_models_for_query

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    route = route_query(request.query)
        
    sources = []

    if route == "knowledge_base":
        kb_results = search_kb(request.query)
        sources = [
            {
                "id": doc["id"],
                "title": doc["title"],
                "score": 1.0,
            }
            for doc in kb_results
        ]
        
    elif route == "huggingface":
        models = search_models_for_query(request.query)
        sources = [
            {
                "id": index,
                "title": model["id"],
                "score": 1.0,
            }
            for index, model in enumerate(models, start=1)
        ]

    return AskResponse(
        answer="",
        confidence=0.0,
        route=route,
        sources=sources,
        query=request.query,
    )