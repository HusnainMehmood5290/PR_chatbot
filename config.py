from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class RAGConfig(BaseSettings):
    # Child document processing
    CHILD_CHUNK_SIZE: int = 200
    CHILD_CHUNK_OVERLAP: int = 50
    # Parent Document
    PARENT_CHUNK_SIZE: int = 4000
    
    # Embeddings
    EMBEDDING_MODEL: str = "sentence-transformers/all-mpnet-base-v2"
    
    # Vector store
    CHILD_STORE: str = "data/processed/child_Store"
    PARENET_STORE: str="data/processed/parent_Store"
    COLLECTION_NAME: str = "hr-policies"
    
    # Raw Document
    RAW_DOCUMENTS: str="data/raw_documents"
    
    # LLM
    LLM_MODEL: str = "gemini-1.5-flash"
    # MAX_OUTPUT_TOKENS: int = 2000
    
    # API keys (loaded from .env)
    GOOGLE_API_KEY: str = Field(..., env="GOOGLE_API_KEY")
    
    # Updated configuration for Pydantic v2
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Singleton configuration instance
config = RAGConfig()