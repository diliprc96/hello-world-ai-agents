# Hello World AI Agents Series

Welcome to the "Hello World" trilogy + combined tutorial on **LangChain**, **LangGraph**, and **Pydantic**.

## Structure
1. **[01-langchain-basics](./01-langchain-basics)**: Minimal ChatOllama usage.
2. **[02-langgraph-flow](./02-langgraph-flow)**: A simple stateful graph.
3. **[03-pydantic-validation](./03-pydantic-validation)**: Structured outputs with Pydantic.
4. **[04-combined-agent](./04-combined-agent)**: A complete pipeline: Draft -> Refine -> Structured Output.

## Global Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com/) running locally.
- `llama3.2` model pulled:
  ```bash
  ollama pull llama3.2
  ```

## Ollama Setup
1. **Install Ollama**: Download from [ollama.com](https://ollama.com/).
2. **Pull the Model**: Open your terminal and run:
   ```bash
   ollama pull llama3.2
   ```
   *Note: You can use other models like `llama3` or `mistral`, but you may need to update the `model=` string in the python scripts.*
3. **Start the Server**: Ensure `ollama serve` is running (usually runs automatically in the background).

## How to Run
1. **Create a Virtual Environment** (Recommended):
   ```bash
   python3 -m venv hello-world-ai-agents
   source hello-world-ai-agents/bin/activate
   ```
2. **Navigate to a Tutorial Folder**:
   ```bash
   cd 01-langchain-basics
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Code**:
   ```bash
   python main.py
   ```
