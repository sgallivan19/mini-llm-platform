# naive rerank: score candidate by similarity to query embedding
from app.services.openai_client import OpenAIClient
def rerank_candidates(query: str, candidates: list[dict]):
    client = OpenAIClient()
    q_emb = client.embed([query])[0]
    out = []
    for c in candidates:
        # candidate is expected to have 'embedding' key or 'text'
        emb = c.get('embedding') or client.embed([c.get('text','')])[0]
        # cosine similarity
        import math
        dot = sum(a*b for a,b in zip(q_emb, emb))
        norm_q = math.sqrt(sum(a*a for a in q_emb))
        norm_c = math.sqrt(sum(a*a for a in emb))
        score = dot / (norm_q*norm_c+1e-8)
        out.append({**c, "score": score})
    return sorted(out, key=lambda x: x['score'], reverse=True)
