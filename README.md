# PR_chatbot

## Table of Contents
- [PR\_chatbot](#pr_chatbot)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
  - [Ollama Setup](#ollama-setup)
  - [Running the Project](#running-the-project)
  - [Project Structure](#project-structure)
  - [License](#license)

## Introduction
PR_chatbot is a Retrieval-Augmented Generation (RAG) system designed for HR policy analysis. It processes PDF documents, stores embeddings, and retrieves relevant information based on user queries.

## Prerequisites
- Python 3.11
- Docker (optional, for containerized deployment)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/HusnainMehmood5290/PR_chatbot.git
    cd PR_chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Setting Up Environment Variables
Create a `.env` file in the root directory of the project with the following content:
```
GOOGLE_API_KEY=your_google_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```
Replace `your_google_api_key`, `your_langsmith_api_key`,  with your actual API keys.

## Ollama Setup
1. download the Ollama from official site:
    ```sh
    https://ollama.com/download/OllamaSetup.exe
    ```

2. Verify the installation through cmd:
    ```sh
    ollama --version
    ```

3. after installation open cmd and run this cmd:
    ```sh
    ollama run gemma3
    ```

## Running the Project
1. store the Manual pdfs in:
    ```sh
    data/raw_documents/emaxple.pdf
    ```

2. Start the main process:
    ```sh
    python -m src/core/ingest.py
    ```

3. Run the Streamlit UI:
    ```sh
    streamlit run ui.py
    ```

## Project Structure
```
PR_chatbot/
├── .env
├── .gitignore
├── config.py
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── template.py
├── ui.py
├── data/
│   ├── processed/
│   │   └── child_store/
│   └── raw_documents/
│       ├── _finalHR.pdf
│       └── .gitkeep
├── scripts/
│   ├── console_test.py
│   └── initialize_vectorstore.py
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ingest.py
│   │   ├── models.py
│   │   ├── rag_chain.py
│   │   └── retriever.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_rag.py
│   │   └── test_retriever.py
│   └── utils/
│       ├── __init__.py
│       ├── chunkers.py
│       ├── file_loader.py
│       └── helpers.py
└── __pycache__/
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
