import os
from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
import requests
from dotenv import load_dotenv

load_dotenv()


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

search_tool=DuckDuckGoSearchRun()

template="""
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""
prompt=PromptTemplate.from_template(template)


@tool
def get_weather_condition(city:str)->str:
    """Fetch the weather condition of a given city"""
    api_key = os.getenv("WEATHER_API_KEY")
    url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city
    }
    response=requests.get(url,params=params)
    return response.json()

agent=create_react_agent(
    llm=llm,
    tools=[search_tool,get_weather_condition],
    prompt=prompt
)

agent_execute=AgentExecutor(
    agent=agent,
    tools=[search_tool,get_weather_condition],
    verbose=True,
    handle_parsing_errors=True
)

result=agent_execute.invoke({"input":"What is the weather condition of Bhilai and also tell me the temperature of Bhilai?"})
#print(result["output"])
print(result)
print(result["output"])
