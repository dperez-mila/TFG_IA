
from dataclasses import dataclass

from .model import Model


@dataclass
class Association(Model):
    rubric_id: str
    associated_object_key: str
    associated_object_type: type[Model]

