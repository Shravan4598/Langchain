from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r"C:\Users\shrav\Desktop\Langchain code\9.RAG\1.Document_Loader\pypdf.pdf")

docs=loader.load()
print(docs)
print("======"*10)
print(len(docs))
print("======"*10)
print(docs[0].page_content)
print("======"*10)
print(docs[0].metadata)