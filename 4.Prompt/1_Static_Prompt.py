from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


static_prompt="Summarize the Attention is all you need paper in the simple terminilogy"
response=model.invoke([HumanMessage(content=static_prompt)])
print(response.content)