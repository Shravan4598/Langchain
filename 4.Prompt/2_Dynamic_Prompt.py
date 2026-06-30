from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = ChatPromptTemplate.from_template("""
You are a {role} on {date}. {action} the paper titled "{paper_title}" in a {style} style.
""")

formatted_prompt = template.format_prompt(
    role="Research Assistant",
    date="22nd March 2004 00:01",
    action="summarize",
    paper_title="Attention Is All You Need",
    style="simple"
)

response = model.invoke(formatted_prompt.to_messages())

print(response.content)