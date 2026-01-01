import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.llm import get_llm
from tools.web_search import web_search

def domain_scout(state):
    topic = state.get("user_topic", "AI healthcare")

    search_results = web_search(
        f"emerging scientific research domains after 2024 in {topic}"
    )

    prompt = f"""
You are a research analyst.

Identify 5 emerging scientific domains (post-2024) related to:
{topic}

Use the information below:
{search_results}

Return bullet points with justification.
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return {
        **state,
        "domains": response.content
    }
