
from dataclasses import dataclass, field

from .model import Model
from .rubric import Rubric
from .submission import Submission


@dataclass
class Assignment(Model):
    name: str
    description: str
    max_score: float
    course_id: str
    rubric: Rubric | None = None
    submissions: list[Submission] = field(default_factory=list)

