
from dataclasses import dataclass

from .model import Model


@dataclass
class Rating(Model):
    description: str
    long_description: str
    max_score: float
    criterion_id: str

    