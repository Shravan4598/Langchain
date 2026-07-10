from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


#Defining model
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#tool decorator
@tool
def multiply(a:int,b:int)->int:
    """Multiply two number"""
    return a*b


#tool binding
llm_with_bind=llm.bind_tools([multiply])


#defining query
query="What is the multiplication of 5 and 3?"
messages=[HumanMessage(query)]

ai_messages=llm_with_bind.invoke(messages)
messages.append(ai_messages)

#tool calling
tool_call=ai_messages.tool_calls[0]

#tool execution
tool_result=multiply.invoke(tool_call)
messages.append(tool_result)

#Final Response
response=llm_with_bind.invoke(messages)
print(response.content)

""" 
The multiplication of 5 and 3 is 15.
"""

print("--------"*20)


print(messages)

"""
[HumanMessage(content='What is the multiplication of 5 and 3?', additional_kwargs={}, response_metadata={}),

 AIMessage(content='', additional_kwargs={'function_call': {'name': 'multiply', 'arguments': '{"a": 5, "b": 3}'}, '__gemini_function_call_thought_signatures__': {'57873d13-0f73-48bd-83a8-11f387c25ad5': 'CtgBARFNMg8Xk2g3nm/LxWQB3T394W1pJbgM8b/LGQy0/QpgbcIQQHDrAhil82n5eS8APBQShjWVwn7e6xNKz4TRSD85bJRxUu6qWovhxCh21suE2anLHlS8D2ZFKO99rIsem9IX7RuZz/Z86iqaqMDvqLihgCsr596+7yP+tlJUzSWZ3fsAsbQb460Pwrzf9rPmxjlO8owX6tfNPiXx+7ALtr9VlSBZwSMkJklWEl5wiQ+LJCYfCeQQ8JMcbn5QTf/N1eRsHQKJrwnaDZb+M6s3txq2hnP0PZgC'}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--019f4cb4-8843-7c42-affa-29e3c8bd3400-0', tool_calls=[{'name': 'multiply', 'args': {'a': 5, 'b': 3}, 'id': '57873d13-0f73-48bd-83a8-11f387c25ad5', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 56, 'output_tokens': 67, 'total_tokens': 123, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 49}}),

 ToolMessage(content='15', name='multiply', tool_call_id='57873d13-0f73-48bd-83a8-11f387c25ad5')]
"""