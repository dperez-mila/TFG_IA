
from dataclasses import dataclass

from .model import Model
from ..enums import EnrollmentType

@dataclass
class Enrollment(Model):
    course_id: str
    user_id: str
    type: EnrollmentType

