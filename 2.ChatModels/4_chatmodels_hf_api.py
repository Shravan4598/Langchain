from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of India?")
print(result)
print(result.content)  # Print the content of the response