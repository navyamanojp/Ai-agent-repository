from langchain_ollama import OllamaLLM

#Load AI Model from Ollama
llm = OllamaLLM(model="mistral")

print("\n Welcome to your ai agent ! ask me anything")
while True:
    question=input("Your Question (or type 'exit' to stop):")
    if question.lower() == 'exit' :
        print("goodbye")
        break
    response = llm.invoke(question)
    print("\n ai response : ",response)