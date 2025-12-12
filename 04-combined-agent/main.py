from typing import TypedDict, List
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field

# --- 1. Define Pydantic Model (The "Contract") ---
class BlogPost(BaseModel):
    title: str = Field(description="Catchy title")
    content: str = Field(description="The main blog post content, under 100 words")
    tags: List[str] = Field(description="3 relevant tags")

# --- 2. Define State ---
class State(TypedDict):
    topic: str
    raw_draft: str
    final_post: BlogPost

# --- 3. Setup LLM ---
llm = ChatOllama(model="llama3.2")
# Create a structured LLM for the final node
structured_llm = llm.with_structured_output(BlogPost)

# --- 4. Define Nodes ---

def draft_node(state: State):
    print(f"--- ✍️  Drafting post about {state['topic']} ---")
    msg = HumanMessage(content=f"Write a short, rough draft for a blog post about {state['topic']}.")
    response = llm.invoke([msg])
    return {"raw_draft": response.content}

def refine_node(state: State):
    print("--- 🎨 Refining and Formatting ---")
    # We ask the structured LLM to strict parse the raw draft + topic into our Schema
    msg = HumanMessage(content=f"Refine this draft into a polished blog post structure. Draft: {state['raw_draft']}")
    response = structured_llm.invoke([msg])
    return {"final_post": response}

# --- 5. Build Graph ---
builder = StateGraph(State)
builder.add_node("drafter", draft_node)
builder.add_node("refiner", refine_node)

builder.add_edge(START, "drafter")
builder.add_edge("drafter", "refiner")
builder.add_edge("refiner", END)

# --- 6. Compile and Run ---
graph = builder.compile()

print("--- 🚀 Starting Combined Agent ---")
result = graph.invoke({"topic": "LangChain and LangGraph"})

post = result["final_post"]
print(f"\nTitle: {post.title}")
print(f"Content: {post.content}")
print(f"Tags: {post.tags}")
