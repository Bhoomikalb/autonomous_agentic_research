def web_search(query: str):
    """
    Dummy web search replacement.
    This allows the agent to run without Tavily.
    """
    return [
        {
            "title": "Offline Search Disabled",
            "content": f"No live web search. Topic received: {query}"
        }
    ]
