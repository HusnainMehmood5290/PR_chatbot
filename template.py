import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "hr-policy-rag/Dockerfile",
    "hr-policy-rag/requirements.txt",
    "hr-policy-rag/pyproject.toml",
    "hr-policy-rag/.env",
    "hr-policy-rag/config.py",
    "hr-policy-rag/README.md",

    "hr-policy-rag/data/raw_documents/.gitkeep",  # To ensure directory exists in Git
    "hr-policy-rag/data/processed/.gitkeep",
    "hr-policy-rag/data/processed/chroma/.gitkeep",  # or pinecone
    "hr-policy-rag/data/processed/json_cache/.gitkeep",

    "hr-policy-rag/src/hr_policy_rag/__init__.py",

    "hr-policy-rag/src/hr_policy_rag/core/__init__.py",
    "hr-policy-rag/src/hr_policy_rag/core/models.py",
    "hr-policy-rag/src/hr_policy_rag/core/vector_store.py",
    "hr-policy-rag/src/hr_policy_rag/core/retriever.py",
    "hr-policy-rag/src/hr_policy_rag/core/rag_chain.py",

    "hr-policy-rag/src/hr_policy_rag/utils/__init__.py",
    "hr-policy-rag/src/hr_policy_rag/utils/file_loader.py",
    "hr-policy-rag/src/hr_policy_rag/utils/chunkers.py",
    "hr-policy-rag/src/hr_policy_rag/utils/helpers.py",

    "hr-policy-rag/src/hr_policy_rag/frontend/__init__.py",
    "hr-policy-rag/src/hr_policy_rag/frontend/ui.py",

    "hr-policy-rag/src/hr_policy_rag/tests/__init__.py",
    "hr-policy-rag/src/hr_policy_rag/tests/test_retriever.py",
    "hr-policy-rag/src/hr_policy_rag/tests/test_rag.py",

    "hr-policy-rag/scripts/initialize_vectorstore.py",
    "hr-policy-rag/scripts/console_test.py",
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