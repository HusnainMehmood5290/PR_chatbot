import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "Dockerfile",
    "requirements.txt",
    "pyproject.toml",
    ".env",
    "config.py",
    "README.md",

    "data/raw_documents/.gitkeep",  # To ensure directory exists in Git
    "data/processed/.gitkeep",
    "data/processed/chroma/.gitkeep",  # or pinecone
    "data/processed/json_cache/.gitkeep",

    "src/hr_policy_rag/__init__.py",

    "src/hr_policy_rag/core/__init__.py",
    "src/hr_policy_rag/core/models.py",
    "src/hr_policy_rag/core/vector_store.py",
    "src/hr_policy_rag/core/retriever.py",
    "src/hr_policy_rag/core/rag_chain.py",

    "src/hr_policy_rag/utils/__init__.py",
    "src/hr_policy_rag/utils/file_loader.py",
    "src/hr_policy_rag/utils/chunkers.py",
    "src/hr_policy_rag/utils/helpers.py",

    "src/hr_policy_rag/frontend/__init__.py",
    "src/hr_policy_rag/frontend/ui.py",

    "src/hr_policy_rag/tests/__init__.py",
    "src/hr_policy_rag/tests/test_retriever.py",
    "src/hr_policy_rag/tests/test_rag.py",

    "scripts/initialize_vectorstore.py",
    "scripts/console_test.py",
]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")