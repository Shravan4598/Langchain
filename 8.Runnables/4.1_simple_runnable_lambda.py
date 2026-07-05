from langchain_core.runnables import RunnableLambda

def word_count(text):
    return len(text.split())

runnable_word_count=RunnableLambda(word_count)

result=runnable_word_count.invoke("Hello Everyone, I am Shravan Kumar Pandey")
print(result)