from langchain_community.chat_models import ChatOllama

from .config import settings


def get_chat_model():
    return ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url = settings.OLLAMA_BASE_URL
    )