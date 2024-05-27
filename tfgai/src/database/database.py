
from abc import ABC, abstractmethod

class DataManagement(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute_query(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def fetch_results(self):
        pass

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exec_type, exec_value, tb):
        self.close()
    
