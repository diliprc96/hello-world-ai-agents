# Part 3: Pydantic Validation

Demonstrates how to use Pydantic models to force the LLM to return structured JSON data, parsed automatically into Python objects.

## Concept
Instead of getting a string back, we get a `Joke` object with `setup`, `punchline`, and `rating` fields.

## Run
```bash
pip install -r requirements.txt
python main.py
```
