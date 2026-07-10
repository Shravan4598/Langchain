from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r"C:\Users\shrav\Desktop\Langchain code\9.RAG\dl-curriculum.pdf")

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=12,
    separator="\n\n"
)

result=splitter.split_documents(docs)
print(result[0].page_content)