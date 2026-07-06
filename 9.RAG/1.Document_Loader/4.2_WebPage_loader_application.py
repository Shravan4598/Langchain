from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

url="https://en.wikipedia.org/wiki/Data_science"

loader=WebBaseLoader(url)

docs=loader.load()

content=docs[0].page_content

prompt=PromptTemplate(
    template="Give me answer of the {question} from the {text}",
    input_variables=["question","text"]
)
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

chain=prompt|model|parser

result=chain.invoke({"question":"What is Data Science","text":content})
print(result)



"""
Question: What is Data Science?

Answer: Based on the provided Wikipedia article, Data Science can be defined as:

Data science is an **interdisciplinary academic field** that utilizes:
*   **Statistics**
*   **Scientific computing**
*   **Scientific methods**
*   **Processing**
*   **Scientific visualization**
*   **Algorithms**
*   **Coding** (like Python, SQL, and R)
*   **Systems**

Its primary purpose is to **extract or extrapolate knowledge from potentially noisy, structured, or unstructured data.**

More broadly, data science is:
*   A **concept to unify statistics, data analysis, informatics, and their related methods** to "understand and analyze actual phenomena" with data.
*   A **multidisciplinary field** that draws techniques and theories from mathematics, statistics, computer science, information science, and domain knowledge.
*   Focused on **extracting knowledge from typically large datasets** and **applying that knowledge to solve problems in other application domains.**
*   Encompasses **preparing data for analysis, formulating data science problems, analyzing data, and summarizing these findings.**
*   It plays a **critical role in modern decision-making** by enabling organizations to extract actionable insights from large and complex datasets.

"""