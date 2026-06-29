from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.9)
result = chat_model.invoke("What is the capital of India?")
print(result)
print(result['content'])  # Print the content of the response
print(result.content)  # Print the content of the response