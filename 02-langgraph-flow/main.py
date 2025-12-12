from typing import TypedDict
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

# 1. Define State
class State(TypedDict):
    topic: str
    joke: str
    improved_joke: str

# 2. Define Nodes
llm = ChatOllama(model="llama3.2")

def generate_joke(state: State):
    print(f"--- Generating Joke about {state['topic']} ---")
    msg = HumanMessage(content=f"Tell me a short joke about {state['topic']}.")
    response = llm.invoke([msg])
    return {"joke": response.content}

def improve_joke(state: State):
    print("--- Improving Joke ---")
    msg = HumanMessage(content=f"Make this joke funnier and shorter: {state['joke']}")
    response = llm.invoke([msg])
    return {"improved_joke": response.content}

# 3. Build Graph
builder = StateGraph(State)
builder.add_node("generator", generate_joke)
builder.add_node("improver", improve_joke)

builder.add_edge(START, "generator")
builder.add_edge("generator", "improver")
builder.add_edge("improver", END)

# 4. Compile and Run
graph = builder.compile()

print("--- Running Graph ---")
result = graph.invoke({"topic": "AI Agents"})
print(f"\nFinal Result:\n{result['improved_joke']}")
