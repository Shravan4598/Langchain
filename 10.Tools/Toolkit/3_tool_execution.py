from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@tool
def multiply(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

llm_with_tool=llm.bind_tools([multiply])

result=llm_with_tool.invoke(
    "What is the multiplication of 5 and 3?"
)
print("Suggest the tool for this task:",result.tool_calls)
print("Suggest the tool for this task:",result.tool_calls[0])
print("------------"*8)
print("Tool:",result.tool_calls[0]["name"])

print("Arguments(args):",result.tool_calls[0]["args"])

print("LLM Response:",multiply.invoke(result.tool_calls[0]["args"]))

print("------------"*8)
print("Return ToolMessage:")
print(multiply.invoke(result.tool_calls[0]))

"""
Suggest the tool for this task: [{'name': 'multiply', 'args': {'b': 3, 'a': 5}, 'id': 'f4c12f32-4a26-4b83-ae3e-64a0d55f498d', 'type': 'tool_call'}]
Suggest the tool for this task: {'name': 'multiply', 'args': {'b': 3, 'a': 5}, 'id': 'f4c12f32-4a26-4b83-ae3e-64a0d55f498d', 'type': 'tool_call'}
------------------------------------------------------------------------------------------------
Tool: multiply
Arguments(args): {'b': 3, 'a': 5}
LLM Response: 15
------------------------------------------------------------------------------------------------
Return ToolMessage:
content='15' name='multiply' tool_call_id='f4c12f32-4a26-4b83-ae3e-64a0d55f498d'
"""
