from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=GoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

prompt=PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

topic=input("Enter a topic: ")

formatted_prompt=prompt.format(topic=topic)

blog_title=llm.invoke(formatted_prompt)

print("The title of the blog is: ",blog_title)
