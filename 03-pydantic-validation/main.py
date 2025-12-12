from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama

# 1. Define Pydantic Model
class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    rating: int = Field(description="How funny the joke is from 1-10")

# 2. Setup LLM with structured output
# Ensure you have pulled the model first: `ollama pull llama3.2`
llm = ChatOllama(model="llama3.2", temperature=0)
structured_llm = llm.with_structured_output(Joke)

# 3. Invoke
print("--- Generating Structured Joke ---")
response = structured_llm.invoke("Tell me a joke about Python programming.")

# 4. Use the object
print(f"\nSetup: {response.setup}")
print(f"Punchline: {response.punchline}")
print(f"Rating: {response.rating}/10")
