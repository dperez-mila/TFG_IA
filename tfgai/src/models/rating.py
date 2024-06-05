
from dataclasses import dataclass

from .model import Model


@dataclass
class Rating(Model):
    criterion_id: str
    description: str
    long_description: str
    max_score: float

    