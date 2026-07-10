from langchain_community.tools import StructuredTool
from pydantic import Field,BaseModel

class multiply_input(BaseModel):
    a:int=Field(required=True,description="The first number to multiply")
    b:int=Field(required=True,description="The second number to multiply")

def multiply_func(a:int,b:int)->int:
    return a*b

multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    name="Multiply",
    description="Multiply two numbers",
    args_schema=multiply_input
)

result=multiply_tool.invoke({"a":5,"b":3})
print(result)
print("===="*10)

print("Name:",multiply_tool.name)
print("Description:",multiply_tool.description)
print("Arguments:",multiply_tool.args)
print(multiply_tool.args_schema)

print(multiply_tool.args_schema.model_json_schema())

"""
15
========================================
Name: Multiply
Description: Multiply two numbers
Arguments {'a': {'description': 'The first number to multiply', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'The second number to multiply', 'title': 'B', 'type': 'integer'}}
<class '__main__.multiply_input'>
{'properties': {'a': {'description': 'The first number to multiply', 'required': True, 'title': 'A', 'type': 'integer'}, 'b': {'description': 'The second number to multiply', 'required': True, 'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply_input', 'type': 'object'}
"""