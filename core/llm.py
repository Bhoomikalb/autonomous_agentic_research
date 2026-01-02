
from langchain_groq import ChatGroq
import os

def get_llm():
    """
    Returns a ChatGroq LLaMA model instance.
    """
    return ChatGroq(
        model="moonshotai/kimi-k2-instruct",
        temperature=0.3,

        groq_api_key=os.getenv("GROQ_API_KEY") # direct
    )

# Wrapper to mimic `.invoke(prompt)` interface
class LLMWrapper:
    def __init__(self):
        self.llm = get_llm()

    def invoke(self, prompt: str):
        """
        Invoke LLaMA model with a prompt and return an object with `.content`
        """
        response = self.llm([HumanMessage(content=prompt)])
        # Return an object that mimics your previous code
        return type("Response", (), {"content": response.content})()
