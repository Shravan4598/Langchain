from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="generate the explanation of the following joke.\n{text}",
    input_variables=["text"]
)


joke_generation_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_generation_chain,parallel_chain)

result=final_chain.invoke({"topic":"AI"})
print(result)
print(result["joke"])
print(result["explanation"])