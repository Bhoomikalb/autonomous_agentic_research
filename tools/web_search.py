import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def web_search(query: str):
    client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    if not os.getenv("TAVILY_API_KEY"):
        raise ValueError("TAVILY_API_KEY is not set in environment variables")

    return client.search(query)
