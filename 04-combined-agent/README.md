# Part 4: Combined Agent

This example brings it all together:
1. **LangChain/Ollama**: Powers the LLM processing.
2. **LangGraph**: Orchestrates the workflow (Draft -> Refine).
3. **Pydantic**: Ensures the final output is a structured `BlogPost` object, not just text.

## Flow
1. **Drafter**: Writes a rough text draft.
2. **Refiner**: Takes the draft and formats it into a Title, Content, and Tags structure.

## Run
```bash
pip install -r requirements.txt
python main.py
```
