from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests
from langchain_community.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

search_tool=DuckDuckGoSearchRun()
result=search_tool.invoke("News of America and Iran war")
print(result)

llm=ChatGoogleGenerativeAI()
response=llm.invoke("hi")
print(response)