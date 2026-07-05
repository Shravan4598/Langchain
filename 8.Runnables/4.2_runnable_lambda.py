from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough, RunnableLambda

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=["topic"]
)


parser=StrOutputParser()

joke_chain=RunnableSequence(prompt1,model,parser)

def word_count(text):
    return len(text.split())

parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
    }
)

final_chain=RunnableSequence(joke_chain,parallel_chain)
result=final_chain.invoke({"topic":"AI"})

print("joke:",result["joke"])
print("Word Count:",result["word_count"])