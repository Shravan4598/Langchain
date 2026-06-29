from lanchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
chat_model = ChatAnthropic(model_name="claude-2", temperature=0.9)
result = chat_model.invoke("What is the capital of India?")
print(result)
print(result['content'])  # Print the content of the response
print(result.content)  # Print the content of the response 