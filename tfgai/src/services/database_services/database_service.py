
from abc import ABC, abstractmethod
from ...repositories import (
    CourseRepository, 
    AssignmentRepository, 
    RubricRepository, 
    SubmissionRepository
)


class DataManagementService(ABC):
    pass