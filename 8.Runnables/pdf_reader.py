from langchain.documents_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import 
from langchain.vectorstores import  FAISS
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

loader=TextLoader("docs.txt")
documents=loader.load()

text_splitter=RecursiveCharacterTextSplitter()
docs=text_splitter.split_documents(documents)

vector_store=FAISS.from_documents(docs,)
retriver=vector_store.as_retriver()
query="What are the key takeways from the documents"
retrived_docs=retriver.get_relevant_documents(query)
retrived_text="\n".join([doc page_content for doc in retrived_docs])
llm=
prompt=f"Based on the following text,answer the question {query} \n \n {retrived_text}"
answer=llm.predict(prompt)
print("Answer: ",answer)

