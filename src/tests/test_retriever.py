from src.core.retriever import create_parent_retriever
retriever = create_parent_retriever()
from src.utils.helpers import LLM
llm = LLM()

while True:
    query = input("Enter query (press q to quit): ")
    if query == "q":
        break

    # Retrieve context synchronously (assuming invoke returns complete context)
    retrieved = retriever.invoke(query)
    # Start streaming the LLM response
    result_generator = llm.stream(
        f"this is query {query}. this is context {retrieved}. answer the query through context if possible. don't create hallucination."
    )
    
    # Stream the output token by token
    # print("Streaming output: ", end="", flush=True)
    for token in result_generator:
        print(token, end="", flush=True)
    print()  # for a newline after the streaming is complete
