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

    "src/__init__.py",

    "src/core/__init__.py",
    "src/core/models.py",
    "src/core/ingest.py",
    "src/core/retriever.py",
    "src/core/rag_chain.py",

    "src/utils/__init__.py",
    "src/utils/file_loader.py",
    "src/utils/chunkers.py",
    "src/utils/helpers.py",

    "ui.py",

    "src/tests/__init__.py",
    "src/tests/test_retriever.py",
    "src/tests/test_rag.py",

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