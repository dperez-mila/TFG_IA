
from dataclasses import dataclass, field

from .model import Model
from .rubric import Rubric
from .assignment import Assignment
from .enrollment import Enrollment
from .user import User

from ..enums import Language


@dataclass
class Course(Model):
    name: str
    language: Language
    rubrics: list[Rubric] = field(default_factory=list)
    assignments: list[Assignment] = field(default_factory=list)
    users: list[User] = field(default_factory=list)
    
