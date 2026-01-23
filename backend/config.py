from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    # Groq (LLM) settings
    GROQ_MODEL: str = Field(default="openai/gpt-oss-120b")
    GROQ_API_KEY: str = Field(default="")  # Load from .env

    # Embedding model (HuggingFace)
    EMBEDDING_MODEL: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2",
        description="Default HuggingFace embedding model"
    )

    # File system paths
    UPLOAD_DIR: Path = Field(default=Path("data/uploaded"))
    INDEX_DIR: Path = Field(default=Path("data/indexes"))

    # Server settings
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
