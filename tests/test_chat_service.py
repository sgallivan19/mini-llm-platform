import pytest
from unittest.mock import patch
from app.services.chat_service import chat_with_retrieval

@pytest.mark.asyncio
async def test_chat_with_retrieval():
    # patch qdrant_query and OpenAI client
    with patch('app.utils.qdrant_client.qdrant_query') as qmock,          patch('app.services.openai_client.OpenAIClient.chat_completion') as cmock:
        qmock.return_value = [{'payload': {'text':'doc text'}}]
        cmock.return_value = 'answer'
        ans = await chat_with_retrieval('hello')
        assert ans == 'answer'
