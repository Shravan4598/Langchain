from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)
documents=[
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Ranchi is the capital of Jharkhand"
]
embedding_vector = embeddings.embed_documents(documents)
print(embedding_vector)  # Print the embedding vector