import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    pipeline_kwargs={"max_length": 100, "temperature": 0.6}
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result)  
print(result.content)  # Print the content of the response