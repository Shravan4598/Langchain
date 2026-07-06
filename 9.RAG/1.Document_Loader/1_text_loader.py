from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template="Write a summary For the following poem.\n{poem}",
    input_variables=["poem"]
)

parser=StrOutputParser()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")



loader=TextLoader(r"C:\Users\shrav\Desktop\Langchain code\9.RAG\1.Document_Loader\cricket.txt",encoding="utf-8")

docs=loader.load()
print(docs)
print("===="*10)
print(type(docs)) # <class 'list'>
print("===="*10)
print(docs[0])
print("===="*10)
print(type(docs[0])) # <class 'langchain_core.documents.base.Document'>

print("===="*10)

chain=prompt|model|parser

result=chain.invoke({"poem":docs[0].page_content})
print(result)