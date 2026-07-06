# from langchain_text_splitters import SemanticChunker
# from langchain_openai.embeddings import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# text_splitter = SemanticChunker(
#     OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=3
# )

# sample = """
# Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


# Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
# """

# docs = text_splitter.create_documents([sample])
# print(len(docs))
# print(docs)


from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Pick a model to understand text meaning
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Setup the semantic chunker
text_splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="percentile"
)

# 3. Create your text
long_text = "Your very long document goes here. The weather in Bhilai is hot today. But the monsoon season brings rain. AI models are very smart. They learn from data."

# 4. Split the text into meaningful chunks
chunks = text_splitter.create_documents([long_text])

# 5. Print the results
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk.page_content}")
