from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)
embedding_vector = embeddings.embed_query("Delhi is the capital of India")
print(embedding_vector)  # Print the embedding vector