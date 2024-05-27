
from .attachment import Attachment
from .assessment import Assessment


class Submission:

    def __init__(self, id: str, assignment_id: str, student_id: str,  grader_id: str, score: float,
                 late: bool,  attachment: Attachment = None, assessments: list[Assessment] = [],
                 visibility: dict = None):
        self._id = id
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._grader_id = grader_id
        self._score = score
        self._late = late
        self._attachment = attachment
        self._assessments = assessments
        self._visibility = visibility

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def assignment_id(self):
        return self._assignment_id
    
    @assignment_id.setter
    def assignment_id(self, assignment_id: str):
        self._assignment_id = assignment_id

    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, student_id: str):
        self._student_id = student_id

    @property
    def grader_id(self):
        return self._grader_id
    
    @grader_id.setter
    def grader_id(self, grader_id: str):
        self._grader_id = grader_id

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score: float):
        self._score = score

    @property
    def late(self):
        return self._late
    
    @late.setter
    def late(self, late: bool):
        self._late = late

    @property
    def attachment(self):
        return self._attachment
    
    @attachment.setter
    def attachment(self, attachment: Attachment):
        self._attachment = attachment

    @property
    def assessments(self):
        return self._assessments
    
    @assessments.setter
    def assessments(self, assessments: list[str]):
        self._assessments = assessments

    def __str__(self) -> str:
        submission_info = []
        submission_info.append("Informació de l'entrega de l'estudiant:")
        submission_info.append(f"\t- Puntuació final assignada pel professor: {self._score}")
        submission_info.append(f"\t- Valoracions del professor a partir dels criteris de la rúbrica:")
        for assessment in self._assessments:
            submission_info.append(str(assessment))
        return '\n'.join(submission_info)
    
    def get_last_attachment(self):
        return self._attachments[-1]
    
    