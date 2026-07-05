from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough



passthrough=RunnablePassthrough()

print(passthrough.invoke({"name":"Shravan"}))
print(passthrough.invoke(2)) # jo input leta hai wahi output deta hai

# Input : {'name': 'Shravan'}
# Output : {'name': 'Shravan'}

# Input: 2
# Output: 2