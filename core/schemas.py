from pydantic import BaseModel
from typing import List

class Domain(BaseModel):
    name: str
    reason: str

class ResearchQuestion(BaseModel):
    question: str
    novelty: int
    feasibility: int

class ExperimentResult(BaseModel):
    hypothesis: str
    method: str
    p_value: float
    effect_size: float
