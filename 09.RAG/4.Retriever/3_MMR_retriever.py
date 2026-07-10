from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vector_store=FAISS.from_documents(
    documents=docs,
    embedding=embedding
)

retriever=vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "lambda_mult":1
    }
)

query="What is langchain?"
result=retriever.invoke(query)

for i,doc in enumerate(result):
    print("===="*10,"Result",i+1,"==="*10)
    print("Content:",doc.page_content)

# lambda_mult=0.5
"""
retriever=vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "lambda_mult":0.5
    }
)
"""

"""
======================================== Result 1 ==============================
Content: LangChain supports Chroma, FAISS, Pinecone, and more.
======================================== Result 2 ==============================
Content: LangChain is used to build LLM based applications.
======================================== Result 3 ==============================
Content: Embeddings are vector representations of text.
"""

# lambda_mult=1
"""
retriever=vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "lambda_mult":1
    }
)
"""
"""
======================================== Result 1 ==============================
Content: LangChain supports Chroma, FAISS, Pinecone, and more.
======================================== Result 2 ==============================
Content: LangChain is used to build LLM based applications.
======================================== Result 3 ==============================
Content: LangChain makes it easy to work with LLMs.
"""