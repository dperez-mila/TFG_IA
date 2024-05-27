
from .submission import Submission


class Assignment():

    def __init__(self, id: str, course_id: str, rubric_id: str, name: str, description: str, 
                 max_score: float, submissions: list[str] = []):
        self._id = id
        self._course_id = course_id
        self._rubric_id = rubric_id
        self._name = name
        self._description = description
        self._max_score = max_score
        self._submissions = submissions

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
    def rubric_id(self) -> str:
        return self._rubric_id
    
    @rubric_id.setter
    def rubric_id(self, rubric_id: str):
        self._rubric_id = rubric_id

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def max_score(self) -> float:
        return self._max_score
    
    @max_score.setter
    def max_score(self, max_score: float):
        self._max_score = max_score

    @property
    def submissions(self) -> list[str]:
        return self._submissions
    
    @submissions.setter
    def submissions(self, **submissions):
        if any(not isinstance(submission, str) for submission in submissions):
            raise TypeError("All the parameters must be submissions' ids (string)!")
        self._submissions.extend(submissions)

    def __str__(self) -> str:
        assignment_info = []
        assignment_info.append("Informació de l'activitat avaluable:")
        assignment_info.append(f"\t- Nom de l'activitat: {self._name}")
        assignment_info.append(f"\t- Descripció de l'activitat: {self._description}")
        assignment_info.append(f"\t- Puntuació màxima de l'activitat: {self._max_score}")
        return '\n'.join(assignment_info)