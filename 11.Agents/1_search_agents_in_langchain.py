from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor,create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests
from langchain_community.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

search_tool=DuckDuckGoSearchRun()


template = """Answer the following questions as best you can.

You have access to the following tools:

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

prompt = PromptTemplate.from_template(template)


agent=create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt,
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

response=agent_executor.invoke({"input":"Tell me  three ways to reach Bhilai from Ranchi"})
print(response["output"])




# print(response)
"""
{'input': 'Tell me  three ways to reach Bhilai from Ranchi', 'output': 'Three ways to reach Bhilai from Ranchi are:\n1.  **By Flight:** This is the fastest way, taking approximately 6 hours (often via Raipur or Jharsuguda).\n2.  **By Train:** This is often the cheapest way and takes around 10-14 hours. Trains run daily.\n3.  **By Bus:** This option takes approximately 12-14 hours.'}
"""

# print(response["output"])
"""
Three ways to reach Bhilai from Ranchi are:
1.  **By Bus:** There are bus services, such as Royal Travels, that operate from Ranchi to Durg (which is very close to Bhilai).
2.  **By Train:** While direct trains might be limited, it is possible to travel by train, often involving transfers at junctions like Tatanagar (TATA) or Titlagarh, to reach Bhilai.
3.  **By Car/Taxi:** One can travel by private car or hire a taxi for a direct road journey from Ranchi to Bhilai.
"""