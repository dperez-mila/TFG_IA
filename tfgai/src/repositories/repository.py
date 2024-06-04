
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ..models import Model


T = TypeVar('T', bound=Model)

class Repository(Generic[T], ABC):

    @abstractmethod
    def add(self, obj: T):
        pass

    @abstractmethod
    def get(self, obj_id: str = None, **conditions) -> T:
        pass

    @abstractmethod
    def update(self, obj_id: str, obj: T):
        pass

    @abstractmethod
    def delete(self, obj_id: str):
        pass

