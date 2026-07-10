from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat_history = [
    system_message := SystemMessage(content="You are a helpful assistant that always responds in a friendly tone.")
]

while True:
    user_input=input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("Bot: ", response.content)

print("\nChat History:", chat_history)
