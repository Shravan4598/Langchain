from langchain_community.document_loaders import WebBaseLoader

url="https://en.wikipedia.org/wiki/Data_science"

loader=WebBaseLoader(url)

docs=loader.load()

print(docs)
print(type(docs[0]))
print(docs[0].page_content)