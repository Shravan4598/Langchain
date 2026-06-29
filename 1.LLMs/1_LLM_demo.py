from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.9)
result=llm.invoke("What is the capital of India?")
print(result)