from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from src.core.retriever import create_parent_retriever
from src.utils.helpers import LLM


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are the SNGPL AI HR Assistant. "),
        ("human", "This is input: {input}. This is context: {context}. Answer the query using the context if possible. Do not create hallucinations or make up information that isn't in the context. If you use information from the context, please cite your source.")
    ]
)

# Define the retrieval chain
llm=LLM()
retriever=create_parent_retriever()
llm_with_customPrompt = create_stuff_documents_chain(
    llm, prompt
)
retrieval_chain = create_retrieval_chain(retriever, llm_with_customPrompt)


# def chain(query):
#     retrieved = retriever.invoke(query)
#     # Start streaming the LLM response
#     result_generator = llm.stream(
#         f"this is query {query}. this is context {retrieved}. answer the query through context if possible. don't create hallucination."
#         )

#         # Stream the output token by token
#         # print("Streaming output: ", end="", flush=True)
#     for token in result_generator:
#         print(token, end="", flush=True)
#     print()  # for a newline after the streaming is complete