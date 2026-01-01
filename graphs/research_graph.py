import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.graph import StateGraph
from agents.domain_scout import domain_scout
from agents.question_generator import question_generator
from agents.data_alchemist import data_alchemist
from agents.experiment_designer import experiment_designer
from agents.critic import critic_agent  # ✅ updated import to match file name

# Create StateGraph
graph = StateGraph(dict)

graph.add_node("domain", domain_scout)
graph.add_node("question", question_generator)
graph.add_node("data", data_alchemist)
graph.add_node("experiment", experiment_designer)
graph.add_node("critic", critic_agent)

graph.set_entry_point("domain")
graph.add_edge("domain", "question")
graph.add_edge("question", "data")
graph.add_edge("data", "experiment")
graph.add_edge("experiment", "critic")

compiled_graph = graph.compile()  # compile once

# Full pipeline wrapper
def invoke_full_pipeline(input_state):
    result = compiled_graph.invoke(input_state)

    # Generate Take-Home Assessment style Markdown
    markdown = f"""
# 🧠 Autonomous Agentic Research Assistant Report

## Assessment Title
Build a Fully Autonomous Agentic AI Research Assistant for Emerging Scientific Domains

## Research Topic
{input_state.get("user_topic", "N/A")}

## 1. Emerging Scientific Domains
{result.get('domains', 'No domains found.')}

## 2. Research Questions
{result.get('questions', 'No questions generated.')}

## 3. Data Acquisition & Cleaning
{result.get('data', {}).get('clean_data', 'No data collected.')}

## 4. Experiment Design
{result.get('experiment', 'No experiment designed.')}

## 5. Critique & Recommendations
{result.get('critic', 'No critique available.')}
"""

    return markdown

# Final app wrapper
class FullResearchApp:
    def invoke(self, input_state):
        return invoke_full_pipeline(input_state)

app = FullResearchApp()
