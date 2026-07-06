from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path=r"C:\Users\shrav\Desktop\Langchain code\9.RAG\Book",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()
print(type(docs))
print("====="*10)
docs=list(docs)
print(len(docs))
print(type(docs))
print(docs[6])
print("====="*10)
print(docs[6].page_content)
print("====="*10)
print(docs[6].metadata)