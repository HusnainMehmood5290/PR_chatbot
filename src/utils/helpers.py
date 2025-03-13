from src.core.models import Models
model=Models()

def LLM():
    return model.ollama_llm

def embeddings():
    return model.embeddings_HuggingFace