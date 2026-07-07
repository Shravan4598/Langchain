from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

vector_store=Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="my_collection"
)

retriever=vector_store.as_retriever(search_kwargs={"k":2})

query="What is Chroma used for?"
result=retriever.invoke(query)

for i,doc in enumerate(result):
    print("==="*5,"Result",i+1,"==="*5)
    print("Content: ",do)