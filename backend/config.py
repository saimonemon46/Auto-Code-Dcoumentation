from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    # Ollama (LLM) settings
    OLLAMA_MODEL: str = Field(default="llama3")  # Default Ollama model
    OLLAMA_BASE_URL: str = Field(default="http://localhost:11434")

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
