
from dataclasses import dataclass, field

from .model import Model
from .criterion import Criterion
from .assessment import Assessment
from .association import Association


@dataclass
class Rubric(Model):
    course_id: str
    assignment_id: str
    title: str
    max_score: float
    associations: list[Association] = field(default_factory=list)
    criterions: list[Criterion] = field(default_factory=list)

