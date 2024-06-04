
from dataclasses import dataclass, field

from .model import Model
from .rating import Rating

@dataclass
class Criterion(Model):
    description: str
    long_description: str
    max_score: float
    rubric_id: str
    ratings: list[Rating] = field(default_factory=list)

   