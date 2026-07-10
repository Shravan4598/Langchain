from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

results=search_tool.invoke("Who won ipl 2026")
print(results)

