import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.llm import get_llm

def experiment_designer(state):
    data = state.get("clean_data")

    if not data:
        return {**state, "experiment": "No data to design experiment."}

    prompt = f"""
Using the following data:
{data}

1. Propose a hypothesis
2. Design an experiment
3. Mention metrics and assumptions
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return {
        **state,
        "experiment": response.content
    }
