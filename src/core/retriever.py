import os
from langchain.storage import LocalFileStore
from langchain.storage._lc_store import create_kv_docstore
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
from config import config
from src.utils.helpers import embeddings
embedding=embeddings()

def create_parent_retriever():
    """Creates and returns a ParentDocumentRetriever instance."""
    try:

        #child Store
        local_store = create_kv_docstore(
            LocalFileStore(config.CHILD_STORE)
            )
        
        # parent store
        vector_store = Chroma(
            collection_name=config.COLLECTION_NAME,
            embedding_function=embedding,
            persist_directory=config.PARENT_STORE,
        )

        # Define chunking strategy
        child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHILD_CHUNK_SIZE,
            chunk_overlap=config.CHILD_CHUNK_OVERLAP,
            add_start_index=True,
        )
        parent_splitter = RecursiveCharacterTextSplitter(chunk_size=config.PARENT_CHUNK_SIZE)

        return ParentDocumentRetriever(
            vectorstore=vector_store,
            docstore=local_store,
            child_splitter=child_splitter,
            parent_splitter=parent_splitter,
        )
    except Exception as e:
        print(f"ERROR: Failed to create parent retriever - {e}")
        return None
