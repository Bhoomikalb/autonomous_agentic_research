import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.llm import get_llm

def critic_agent(state):
    experiment = state.get("experiment")

    if not experiment:
        return {**state, "critic": "No experiment to critique."}

    prompt = f"""
You are a ruthless scientific reviewer.

Critique the following experiment:
{experiment}

Identify flaws, statistical issues, and improvements.
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return {
        **state,
        "critic": response.content
    }
