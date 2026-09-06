from fastapi import APIRouter

from app.schemas.ask import AskRequest, AskResponse
from app.services.router import route_query
from app.services.knowledge_base import search_kb
from app.services.huggingface import search_models_for_query
from app.services.llm import generate_answer


router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    route = route_query(request.query)
    sources = []
    context = ""

    if route == "knowledge_base":
        kb_results = search_kb(request.query)

        context = "\n\n".join(
            f"Title: {doc['title']}\nContent: {doc['content']}"
            for doc in kb_results
        )

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

        context = "\n\n".join(
            f"Model: {model['id']}\n"
            f"Downloads: {model['downloads']}\n"
            f"Likes: {model['likes']}"
            for model in models
        )

        sources = [
            {
                "id": index,
                "title": model["id"],
                "score": 1.0,
            }
            for index, model in enumerate(models, start=1)
        ]
        
    if route == "unknown":
        answer = "I don't have enough information to answer this question."
    else:
        prompt = f"""
                    You are a helpful AI learning platform support assistant.

                    Answer the user's question using only the information provided in the context below.

                    If the context does not contain enough information to answer the question, say that you do not have enough information.

                    User question:
                    {request.query}

                    Context:
                    {context}

                    Answer:
                    """

        answer = generate_answer(prompt)

    return AskResponse(
        answer=answer,
        confidence=0.0,
        route=route,
        sources=sources,
        query=request.query,
    )