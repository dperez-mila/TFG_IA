
from dataclasses import dataclass
from abc import ABC


@dataclass
class Model(ABC):
    id: str

