from langchain_groq import ChatGroq
from .config import settings

def get_chat_model():
    return ChatGroq(
        model=settings.GROQ_MODEL,
        groq_api_key=settings.GROQ_API_KEY
    )
