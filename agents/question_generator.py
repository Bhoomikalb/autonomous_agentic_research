import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.llm import get_llm

def question_generator(state):
    domains = state.get("domains")

    if not domains:
        return {**state, "questions": "No domains provided."}

    prompt = f"""
Based on these emerging domains:
{domains}

Generate 3 original research questions.
Rate novelty and feasibility (1–10).
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return {
        **state,
        "questions": response.content
    }
