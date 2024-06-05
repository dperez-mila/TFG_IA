
from dataclasses import dataclass, field

from .model import Model
from .rubric import Rubric
from .submission import Submission


@dataclass
class Assignment(Model):
    course_id: str
    name: str
    max_score: float
    description: str = ""
    rubric: Rubric | None = None
    submissions: list[Submission] = field(default_factory=list)

