from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

result = chat_model.invoke("What is the capital of India?")

print(result)
print(result.content)