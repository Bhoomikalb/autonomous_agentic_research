# agents/data_alchemist.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.scraper import scrape_text

def data_alchemist(state):
    questions = state.get("questions")

    if not questions:
        return {**state, "clean_data": "No questions to collect data for."}

    arxiv = scrape_text("https://arxiv.org")
    github = scrape_text("https://github.com")

    merged = f"""
SOURCE: arXiv
{arxiv}

SOURCE: GitHub
{github}
"""

    return {
        **state,
        "clean_data": merged,
        "data_sources": ["arXiv", "GitHub"]
    }
