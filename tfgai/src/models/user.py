
from dataclasses import dataclass, field

from .model import Model
from .enrollment import Enrollment


@dataclass
class User(Model):
    username: str
    email: str = ""
    full_name: str = ""
    first_name: str = ""
    last_name: str = ""
    enrollments: list[Enrollment] = field(default_factory=list)
    
