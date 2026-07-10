from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(top_k_results=2,lang="en")

query="Tell me about Bhagat Singh Indian freedom fighter"

docs=retriever.invoke(query)

for i,doc in enumerate(docs):
    print()
    print("==="*5,"Result",i+1,"==="*5)
    print("content:",doc.page_content)