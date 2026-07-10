from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@tool
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

llm_with_bind_tools=llm.bind_tools([multiply])

result=llm_with_bind_tools.invoke(
    "What is the product of 5 and 3?"
)
print(result)
print(result.content)
print(result.tool_calls)