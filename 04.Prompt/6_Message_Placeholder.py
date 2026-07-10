from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#chat template
chat_template = ChatPromptTemplate([
    ("system","You are helpful cricket expert"),
    (MessagesPlaceholder(variable_name="chat_history")),
    ("human","{query}")
    ])


# load chat history
chat_history = []
with open("C:\\Users\\shrav\\Desktop\\Langchain code\\4.Prompt\\chat_history.txt") as f:
    chat_history.extend(f.readlines())
print(chat_history)


# create prompt
prompt=chat_template.invoke({"chat_history":chat_history,"query":"Explain in simple terms about dusra."})
print(prompt)