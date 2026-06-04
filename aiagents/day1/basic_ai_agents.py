from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

#Load AI Model from Ollama
llm = OllamaLLM(model="mistral")
#initialize Memory
chat_history = ChatMessageHistory() #stores history
#define ai prompt
prompt=PromptTemplate(
    input_variables=["chat_history","question"],
    template="Previous conversation : {chat_history}\n User : {question}\n ai"
)

#function to run AI chat with memory
def run_chain(question):
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
    # Run the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
    # Store new user input and AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response

print("\n Ai Chatbot with Memory")
print("type 'exit' to stop ")

while True:
    user_input=input("\n You :")
    if user_input().lower() == 'exit' :
        print("goodbye")
        break
    ai_response = run_chain(user_input)
    print("\n AI : ",ai_response)