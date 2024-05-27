
from abc import ABC, abstractmethod
from ..database import DataManagement


class Repository(ABC):
    
    def __init__(self, db_manager: DataManagement):
        self._db_manager = db_manager

    @abstractmethod
    def add(self, item: object):
        pass

    @abstractmethod
    def get(self, identifier: str) -> object:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, item: object):
        pass

    @abstractmethod
    def delete(self, identifier: str):
        pass

