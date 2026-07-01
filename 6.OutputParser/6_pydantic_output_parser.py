from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="Name of the city the person belongs to")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name,age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

chain=template|model|parser
final_result=chain.invoke({"place":"indian"})
print(final_result)








# prompt=template.invoke({"place":"indian"})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(prompt)
# print("===================================================")
# print(final_result)

"""
text='Generate the name,age and city of a fictional indian person \n The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Name of the person", "title": "Name", "type": "string"}, "age": {"description": "Age of the person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"}, "city": {"description": "Name of the city the person belongs to", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'
===================================================
name='Rohit Sharma' age=35 city='Mumbai'
"""