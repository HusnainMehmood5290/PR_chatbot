from src.core.retriever import create_parent_retriever
retriever=create_parent_retriever()
from src.utils.helpers import LLM
llm=LLM()
query=""
while True:
    query=input("Enter query (press q to quit): ")
    if query=="q":
        break
    else:
        
        retrieved=retriever.invoke(query)
        result=llm.invoke(f"this is query{query}. this is context{retrieved}. answer the query through context if possible. don't create hullicination.") 
        print(result.content)
