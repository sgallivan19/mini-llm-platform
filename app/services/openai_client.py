import openai
from app.core.config import settings

class OpenAIClient:
    def __init__(self):
        openai.api_key = settings.openai_api_key

    def chat_completion(self, prompt: str):
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            max_tokens=512,
            temperature=0.2,
        )
        return resp.choices[0].message.content.strip()

    def embed(self, texts: list[str]):
        resp = openai.Embedding.create(model="text-embedding-3-large", input=texts)
        return [r.embedding for r in resp.data]
