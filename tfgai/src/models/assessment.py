
from dataclasses import dataclass

from .model import Model

@dataclass
class Assessment(Model):
    submission_id: str
    rubric_id: str
    association_id: str
    criterion_id: str
    rating_id: str
    score: float
    comments: str = ""

