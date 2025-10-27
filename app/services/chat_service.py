from app.utils.qdrant_client import qdrant_query
from app.services.openai_client import OpenAIClient

async def chat_with_retrieval(query: str):
    hits = qdrant_query(query, top_k=3)
    context = "\n\n".join([h.get('payload', {}).get('text','') for h in hits])
    prompt = f"Use the following documents to answer the question:\n{context}\n\nQuestion: {query}"
    client = OpenAIClient()
    resp = client.chat_completion(prompt)
    return resp
