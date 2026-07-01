from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template="Generate 5 interseting facts about {topic}",
    imput_variables=["topic"]
)
parser=StrOutputParser()

chain=prompt|model|parser

result=chain.invoke({"topic":"IPL"})
print(result)

chain.get_graph().print_ascii() # To visualize the chain
"""

"""