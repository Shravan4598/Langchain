from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
#text="Delhi is the capital of India"
documents=[
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Ranchi is the capital of Jharkhand"
]
vector=embeddings.embed_documents(documents)
print(vector)  # Print the embedding vector
