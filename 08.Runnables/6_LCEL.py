from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnablePassthrough, RunnableLambda,RunnableBranch

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a deailed report on  {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

report_chain=prompt1|model|parser

#number of conditions=number of tuple inside the runnable branch
# branch_chain=RunnableBranch(
#     (condition1,runnable1),
#     (condtion2,runnable2),
#     default_runnable
# )

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,prompt2|model|parser),
    RunnablePassthrough()
)

chain=report_chain|branch_chain

result=chain.invoke({"topic":"India vs Pakistan"})

print(result)