from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


# *   **HumanMessage:** What *you* (the user) say or ask the AI.
# *   **AIMessage:** What the AI model says back as a response.
# *   **SystemMessage:** Instructions or rules given to the AI to guide its overall behavior or persona.

# *   **HumanMessage:** What *you* (the user) say or ask the AI.
#     *   **Example:** "What's the weather like today?"
# *   **AIMessage:** What the AI model says back as a response.
#     *   **Example:** "The weather today is sunny with a high of 75 degrees Fahrenheit."
# *   **SystemMessage:** Instructions or rules given to the AI to guide its overall behavior or persona.
#     *   **Example:** "You are a helpful assistant that always responds in a friendly tone."

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages=[
    system_message := SystemMessage(content="You are a helpful assistant that always responds in a friendly tone."),
    human_message := HumanMessage(content="Tell me about Langchain?")
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
print("==="*25)
print(messages[-1])  # Print the last message, which should be the AI message
