
from dataclasses import dataclass, field

from .model import Model
from .attachment import Attachment
from .assessment import Assessment


@dataclass
class Submission(Model):
    course_id: str
    assignment_id: str
    user_id: str
    late: bool
    score: float = None
    rubric_score: float = None
    attachment: Attachment = None
    assessments: list[Assessment] = field(default_factory=list)

