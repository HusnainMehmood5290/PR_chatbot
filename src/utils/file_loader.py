import pymupdf4llm
from langchain_text_splitters import MarkdownHeaderTextSplitter
from src.core.retriever import create_parent_retriever


headers_to_split_on = [ #this thing store the meta data base on header
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 3"),
        ("#####", "Header 3"),
        ("######", "Header 3"),
    ]

def load_file(file_path):
    """
    Processes a given PDF file:
    1. Converts it to Markdown.
    2. Loads the Markdown into a retriever.
    3. Adds the document to the vector store.
    """
    try:
        md_content=pymupdf4llm.to_markdown(file_path)
        markdwon_splitter=MarkdownHeaderTextSplitter(headers_to_split_on)
        splitted_docs=markdwon_splitter.split_text(md_content)
    except Exception as e:
        print(f"ERROR: while splitting through markdwonHeaderTextSplitter")


    parent_retriever = create_parent_retriever()
    if not parent_retriever:
        print("ERROR: Parent retriever could not be created.")
        return

    try:
        print(f"Adding document {file_path} to retriever...")
        parent_retriever.add_documents(splitted_docs)
        print(f"Adding document {file_path} to retriever Sufessfully")

    except Exception as e:
        print(f"ERROR: Processing failed for {file_path} - {e}")
