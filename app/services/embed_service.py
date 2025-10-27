from app.services.openai_client import OpenAIClient
def embed_texts(texts: list[str]):
    client = OpenAIClient()
    return client.embed(texts)
