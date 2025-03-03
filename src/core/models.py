# from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from config import config
import os


class Models:
    def __init__(self):
        # Initialize only the LLM immediately (if needed)
        self._embeddings_HuggingFace = None
        self._gemini_llm=None

    @property
    def embeddings_HuggingFace(self): #best and fastest + suggested by hugingface
        if self._embeddings_HuggingFace is None:
            try:
                print(f"Initializing HuggingFace Embeddings= {config.EMBEDDING_MODEL}...")
                self._embeddings_HuggingFace = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
            except Exception as e:
                print(f"Error initializing HuggingFace Embeddings= {config.EMBEDDING_MODEL}: {e}")
        return self._embeddings_HuggingFace


    @property
    def gemini_llm(self):
        if self._gemini_llm is None:
            try:
                print(f"Initializing gemini model={config.LLM_MODEL}")
                self._gemini_llm=ChatGoogleGenerativeAI(model=config.LLM_MODEL,api_key=config.GOOGLE_API_KEY)
            except Exception as e:
                print(f"Error initializing gemini model={config.LLM_MODEL}: {e}")
        return self._gemini_llm