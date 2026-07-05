from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="",
    input_variables=[""]
)

prompt2=PromptTemplate(
    template="",
    input_variables=[""]
)

parser=StrOutputParser()

chain=RunnableParallel()