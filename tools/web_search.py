from tavily import TavilyClient

# ⚠️ TEMPORARY: hardcoded key (allowed for local dev)
TAVILY_API_KEY = "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"

client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str):
    return client.search(query)
