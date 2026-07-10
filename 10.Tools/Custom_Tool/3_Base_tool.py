from langchain_community.tools import BaseTool
from pydantic import BaseModel,Field
from typing import Type

class multiply_input(BaseModel):
    a:int=Field(required=True,description="The first number to multiply")
    b:int=Field(required=True,description="The second number to multiply")


class MultiplyTool(BaseTool):
    name:str="Multiply"
    description:str="Multiply two numbers"
    args_schema:Type[BaseModel]=multiply_input

    def _run(self, a:int,b:int)->int:
        return a*b


multiply_tool=MultiplyTool()

result=multiply_tool.invoke({"a":3,"b":5})
print(result)

print("======"*10)
print(multiply_tool.name)
print(multiply_tool.description)
print("Arguments:",multiply_tool.args)
print("======"*10)
print(multiply_tool.args_schema)
print("======"*10)
print(multiply_tool.args_schema.model_json_schema())

"""
15
============================================================
Multiply
Multiply two numbers
Arguments: {'a': {'description': 'The first number to multiply', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'The second number to multiply', 'title': 'B', 'type': 'integer'}}
============================================================
<class '__main__.multiply_input'>
============================================================
{'properties': {'a': {'description': 'The first number to multiply', 'required': True, 'title': 'A', 'type': 'integer'}, 'b': {'description': 'The second number to multiply', 'required': True, 'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply_input', 'type': 'object'}
"""