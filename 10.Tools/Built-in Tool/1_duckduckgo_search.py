from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

results=search_tool.invoke("Shravan Kumar Pandey linkedin")
print(results)

print("Description:",search_tool.description)
print("Name:",search_tool.name)
print("Arguments:",search_tool.args)