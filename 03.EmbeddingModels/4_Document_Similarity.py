from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Sachin Tendulkar is a legendary right-handed batsman with 100 international centuries and over 34,000 international runs.",
    "Virat Kohli is a right-handed batsman with over 27,000 international runs and more than 80 international centuries.",
    "Rohit Sharma is a right-handed batsman and occasional right-arm off-break bowler, known for his record-breaking innings and being the captain of the Indian cricket team.",
    "MS Dhoni is a wicketkeeper-batsman and captain who won the 2007 T20 World Cup, 2011 World Cup, and 2013 Champions Trophy.",
    "Jasprit Bumrah is a right-arm fast bowler known for his yorkers and being one of India's leading wicket-takers across formats."
]

query = "Tell me about Rohit Sharma"

# Generate embeddings
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)

# Print all similarity scores
print("Similarity Scores:")
for i, score in enumerate(scores[0]):
    print(f"Document {i+1}: {score:.4f}")

# Find the most similar document
best_index = np.argmax(scores[0])
best_score = scores[0][best_index]

# Print results
print("\n" + "=" * 50)
print(f"Query: {query}")
print("=" * 50)

print("\nMost Similar Document:")
print(documents[best_index])

print(f"\nHighest Similarity Score: {best_score:.4f}")