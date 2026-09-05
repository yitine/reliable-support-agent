import json
from pathlib import Path

KB_PATH = Path(__file__).parent.parent / "data" / "knowledge_base.json"

def load_knowledge_base():
    with open(KB_PATH, 'r') as f:
        return json.load(f)


# Keyword Retrieval
def search_kb(query: str, top_k: int = 3):
    """Simple keyword-based search (can be enhanced with embeddings later)"""
    kb = load_knowledge_base()
    query_lower = query.lower()
    
    # Score by keyword match in title and content
    scored = []
    for doc in kb:
        score = 0
        if query_lower in doc['title'].lower():
            score += 3
        if query_lower in doc['content'].lower():
            score += 1
        # Also check tags
        for tag in doc['tags']:
            if tag in query_lower:
                score += 2
        
        if score > 0:
            scored.append((score, doc))
    
    # Sort by score and return top_k
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored[:top_k]]