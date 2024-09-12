import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool


@tool  # annotation lets Langchain to convert function to OpenAI function calling structure
def fetch_weather(city: str):
    """Gets the weather for a given city"""  # required docstring
    url = f"https://api.weatherapi.com/v1/current.json?key=e9bdc46fc5284476b6e123517241604&q={city}"
    response = requests.get(url)
    return response.json()["current"]["condition"]["text"]


llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools([fetch_weather])
query = "What's the weather like in Calgary?"
result = llm_with_tools.invoke(query).tool_calls
city = result[0]["args"]["city"]

weather = fetch_weather.invoke(city)
# Could also use the LLM to create a response with the findings
print(f"The current weather in {city} is {weather.lower()}.")
