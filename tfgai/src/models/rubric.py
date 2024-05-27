
from .criterion import Criterion


class Rubric():

    def __init__(self, id: str, course_id: str, title: str, max_score: float, 
                 criteria: list[Criterion] = None, visibility: dict = None):
        self._id = str(id)
        self._course_id = str(course_id)
        self._title = str(title)
        self._max_score = float(max_score)
        self._criteria = criteria
        self._visibility = visibility

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def course_id(self) -> str:
        return self._course_id
    
    @course_id.setter
    def course_id(self, course_id: str):
        self._course_id = course_id

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def max_score(self) -> float:
        return self._max_score
    
    @max_score.setter
    def max_score(self, max_score: float):
        self._max_score = max_score
    
    @property
    def criteria(self):
        return self._criteria
    
    @criteria.setter
    def criteria(self, criteria: list[Criterion]):
        self._criteria = criteria
    
    def get_criterion(self, criterion_id: str):
        for criterion in self._criteria:
            if criterion.id == criterion_id:
                return criterion  
        return None

    def __str__(self) -> str:
        assignment_info = []
        assignment_info.append("Informació de la rúbrica:")
        assignment_info.append(f"\t- Títol de la Rúbrica: {self._title}")
        assignment_info.append(f"\t- Puntuació màxima: {self._max_score}")
        assignment_info.append(f"\t- Criteris de la rúbrica:")
        for criterion in self._criteria:
            assignment_info.append(str(criterion))
        return '\n'.join(assignment_info)

