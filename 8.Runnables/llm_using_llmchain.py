from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=GoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

prompt=PromptTemplate(
    template="Give me the title of the blog on the {topic}",
    input_variables=["topic"]
)

chain=prompt|llm

result=chain.invoke({"topic":"Data Science"})

print(result)