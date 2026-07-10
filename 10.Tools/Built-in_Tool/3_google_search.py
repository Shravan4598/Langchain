from langchain_google_community import GoogleSearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()

search=GoogleSearchAPIWrapper()

response=search.run("Who is Shravan Kumar Pandey on linkedin")
print(response)