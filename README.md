# PR_chatbot

## Table of Contents
- [PR\_chatbot](#pr_chatbot)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
  - [Running the Project](#running-the-project)
  - [Project Structure](#project-structure)
  - [License](#license)

## Introduction
PR_chatbot is a RAG (Retrieval-Augmented Generation) system for HR policy analysis. It processes PDF documents, stores embeddings, and retrieves relevant information based on user queries.

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
Create a [.env](http://_vscodecontentref_/1) file in the root directory of the project with the following content:



Replace `your_google_api_key` with your actual Google API key.

## Running the Project
1. Initialize the vector store:
    ```sh
    python scripts/initialize_vectorstore.py
    ```

2. Start the main process:
    ```sh
    python src/core/ingest.py
    ```

## Project Structure


## License
This project is licensed under the MIT License - see the [LICENSE](http://_vscodecontentref_/2) file for details.
