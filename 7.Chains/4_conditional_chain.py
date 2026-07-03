from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

class Feedback(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

parser1=StrOutputParser()

prompt=PromptTemplate(
    template="Classify the sentiment of the following text into positive or negative. \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

prompt1 = PromptTemplate(
    template="""
You are a customer support assistant.

Write exactly ONE short professional response (2-3 sentences) to the following positive feedback.

Feedback:
{feedback}

Do not provide multiple responses.
Do not provide explanations.
""",
    input_variables=["feedback"]
)

prompt2 = PromptTemplate(
    template="""
You are a customer support assistant.

Write exactly ONE short professional response (2-3 sentences) to the following negative feedback.

Feedback:
{feedback}

Do not provide multiple responses.
Do not provide explanations.
""",
    input_variables=["feedback"]
)

classifier_chain=prompt|model|parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt1|model|parser1),
    (lambda x:x.sentiment=="negative",prompt2|model|parser1),
    RunnableLambda(lambda x:"Could not find sentiment")
)

chain=classifier_chain|branch_chain

print(chain.invoke({"feedback":"This is a beautiful smartphone"}))
print("====="*10)
print(chain.invoke({"feedback":"This is a  terrible smartphone"}))

chain.get_graph().print_ascii()

"""
  +-------------+      
      | PromptInput |      
      +-------------+      
             *             
             *             
             *             
    +----------------+     
    | PromptTemplate |     
    +----------------+     
             *             
             *             
             *             
+------------------------+ 
| ChatGoogleGenerativeAI | 
+------------------------+ 
             *             
             *             
             *             
 +----------------------+  
 | PydanticOutputParser |  
 +----------------------+  
             *             
             *             
             *             
        +--------+         
        | Branch |         
        +--------+         
             *             
             *             
             *             
     +--------------+      
     | BranchOutput |      
     +--------------+      

"""