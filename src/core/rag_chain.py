from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from src.core.retriever import create_parent_retriever
from src.utils.helpers import LLM


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer only using the provided context. If unsure, respond with 'I do not know. can you ask a more clear question?so i can assist you.'"),
        ("human", "Use the user question {input} to answer the question. Use only the {context} to answer the question.")
    ]
)

# Define the retrieval chain
llm=LLM()
retriever=create_parent_retriever()
llm_with_customPrompt = create_stuff_documents_chain(
    llm, prompt
)
retrieval_chain = create_retrieval_chain(retriever, llm_with_customPrompt)
