from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough, RunnableLambda,RunnableBranch

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

report_chain=RunnableSequence(prompt1,model,parser)

#number of conditions=number of tuple inside the runnable branch
# branch_chain=RunnableBranch(
#     (condition1,runnable1),
#     (condtion2,runnable2),
#     default_runnable
# )

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain=RunnableSequence(report_chain,branch_chain)

result=chain.invoke({"topic":"India vs Pakistan"})

print(result)

# Output
"""
The India-Pakistan cricket rivalry is a profound spectacle, transcending sport to embody a complex tapestry of history, politics, culture, and national identity, often dubbed the "mother of all rivalries."
Rooted in the 1947 partition, the rivalry evolved from cautious early Test matches to dynamic One Day Internationals (ODIs) in the 1980s, creating legendary moments like Javed Miandad's Sharjah six. In the new millennium, political tensions frequently suspended bilateral series, making high-stakes ICC tournaments the primary battleground, further intensified by T20 cricket.
More than just a game, it's a cultural phenomenon where national pride is fiercely contested, leading to unparalleled emotional investment from billions of fans. Despite the intensity, it can paradoxically serve as a bridge for social cohesion and always generates immense media frenzy.
On the field, it's a clash of styles: India, historically strong in batting and spin, now boasts formidable all-round capabilities, while Pakistan is renowned for world-class fast bowlers and unpredictable flair. The rivalry is punctuated by numerous iconic moments, from Anil Kumble's 10-wicket haul to Virat Kohli's T20 World Cup heroics.
Statistically, India dominates in World Cup encounters (both ODI and T20), while Pakistan historically leads in overall ODIs and has a slight edge in Tests. The biggest challenge remains political interference, which consistently disrupts bilateral series, forcing matches into neutral venues and ICC tournaments.
Despite these complexities, the rivalry is destined to endure, with new generations of players continuing the saga. Fans and purists perpetually hope for the resumption of full bilateral series, recognizing that this epic contest, while reflecting deep divisions, also ignites unparalleled passion and creates moments that resonate for generations.
"""