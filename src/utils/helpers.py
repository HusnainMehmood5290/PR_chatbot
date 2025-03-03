from src.core.models import Models
model=Models()

def LLM():
    return model.gemini_llm

def embeddings():
    return model.embeddings_HuggingFace