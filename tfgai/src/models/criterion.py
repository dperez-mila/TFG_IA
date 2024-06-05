
from dataclasses import dataclass, field

from .model import Model
from .rating import Rating

@dataclass
class Criterion(Model):
    rubric_id: str
    description: str
    long_description: str
    max_score: float
    ratings: list[Rating] = field(default_factory=list)

   