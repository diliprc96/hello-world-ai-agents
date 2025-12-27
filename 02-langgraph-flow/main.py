from typing import TypedDict
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

# 1. Define State
class State(TypedDict):
    topic: str
    Explanation: str
    Simplified: str

# 2. Define Nodes
llm = ChatOllama(model="llama3.2")

def generate_explanation(State):
    print(f"Generating explanation about {State['topic']}")
    user_query = HumanMessage(content=f"what are {State['topic']}")
    response = llm.invoke([user_query])
    print(response.content)
    return {"Explanation":response.content}

def simplify_explanation(State):
    print(f"Simplifying explanation about")
    user_query = HumanMessage(content=f"Simplify the explanation to 2 to 3 lines. Explanation: {State}")
    response = llm.invoke([user_query])
    print(response.content)
    return {"Simplified":response.content}


builder = StateGraph(State)
builder.add_node("Explain", generate_explanation)
builder.add_node("Simplify", simplify_explanation)

builder.add_edge(START, "Explain")
builder.add_edge("Explain", "Simplify")
builder.add_edge("Simplify", END)

graph = builder.compile()
result = graph.invoke({"topic":"Black holes"})
print(result['Simplified'])


