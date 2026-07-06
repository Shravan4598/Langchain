from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path=r"C:\Users\shrav\Desktop\Langchain code\9.RAG\Book",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(docs)
print("====="*10)
print(len(docs))
print("====="*10)
print(docs[0])
print("====="*10)
print(docs[0].page_content)
print("====="*10)
print(docs[0].metadata)
print("====="*10)
print(docs[38].page_content)