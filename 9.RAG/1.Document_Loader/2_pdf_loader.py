from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r"C:\Users\shrav\Desktop\Langchain code\9.RAG\1.Document_Loader\pypdf.pdf")

docs=loader.load()
print(docs)
print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)