from src.utils.helpers import LLM
llm=LLM()

query=""
while True:
    query=input("Enter query (press q to quit): ")
    if query=="q":
        break
    else:
        
        retrieved=llm.invoke(query)
        print(retrieved)
