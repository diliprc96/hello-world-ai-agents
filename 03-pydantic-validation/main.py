from pydantic import BaseModel
from typing import List
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import json

class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    conditions: str
    forecast: List[str]

llm = ChatOllama(model="llama3.2")

# First prompt with explicit JSON structure
prompt = HumanMessage(content="Generate a weather forecast for Bengaluru in JSON format with the following keys: city, temperature, humidity, conditions, forecast. Example: {\"city\": \"Bengaluru\", \"temperature\": 28.5, \"humidity\": 70, \"conditions\": \"Partly cloudy\", \"forecast\": [\"Sunny\", \"Partly cloudy\", \"Rain\"]}")

response = llm.invoke([prompt])
print("Raw LLM Output:", response.content)

try:
    llm_output = json.loads(response.content)
    validated_weather = WeatherData(**llm_output)
    print("Validated Weather Data:", validated_weather)
except Exception as e:
    print("Validation Error:", e)
    # Create a targeted correction prompt
    error_str = str(e)
    correction_prompt = HumanMessage(content=f"Correct the following JSON to match the schema: {response.content}. Error: {error_str}. Please fix the issue and output only valid JSON with the correct types and keys: city (str), temperature (float), humidity (int), conditions (str), forecast (list of str).")
    correction_response = llm.invoke([correction_prompt])
    print("Corrected LLM Output:", correction_response.content)
    try:
        corrected_output = json.loads(correction_response.content)
        validated_weather = WeatherData(**corrected_output)
        print("Validated Corrected Weather Data:", validated_weather)
    except Exception as e:
        print("Still invalid after correction:", e)
