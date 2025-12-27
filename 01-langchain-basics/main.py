from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# 1. Create the model
# Ensure you have pulled the model first: `ollama pull llama3.2`
llm = ChatOllama(model="llama3.2")

# 2. Define the input
message = HumanMessage(content="what are blackholes?")

# 3. Call the model and stream the response
print("🤖 AI Response:\n")
for chunk in llm.stream([message]):
    print(chunk.content, end="", flush=True)
print("\n")
