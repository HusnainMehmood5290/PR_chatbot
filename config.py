from pydantic_settings import BaseSettings
from pydantic import Field

class RAGConfig(BaseSettings):
    EMBEDDING_MODEL: str = "sentence-transformers/all-mpnet-base-v2"
    LLM_MODEL: str = "gemini-1.5-flash"

    # Splitter
    CHILD_CHUNK_SIZE: int = 250
    CHILD_CHUNK_OVERLAP: int = 30
    PARENT_CHUNK_SIZE: int = 4000

    # Vector store
    CHILD_STORE: str = "data/processed/child_store"
    PARENT_STORE: str = "data/processed/parent_store"
    COLLECTION_NAME: str = "hr-policies"

    # Raw Document
    RAW_DOCUMENTS: str = "data/raw_documents"

    # API keys
    GOOGLE_API_KEY: str = Field(..., env="GOOGLE_API_KEY")
    LANGSMITH_API_KEY: str = Field(..., env="LANGSMITH_API_KEY")
    
    # link to .env file
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

config = RAGConfig()
