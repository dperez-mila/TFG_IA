
class Assessment():

    def __init__(self, id: str, submission_id: str, rubric_id: str, criterion_id: str, rating_id: str, score: float, comment: str = ""):
        self._id = id
        self._submission_id = submission_id
        self._rubric_id = rubric_id
        self._criterion_id = criterion_id
        self._rating_id = rating_id
        self._score = score
        self._comment = comment

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id
        
    @property
    def submission_id(self):
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id: str):
        self._submission_id = submission_id

    @property
    def rubric_id(self):
        return self._rubric_id

    @rubric_id.setter
    def rubric_id(self, rubric_id: str):
        self._rubric_id = rubric_id

    @property
    def criterion_id(self):
        return self._criterion_id
    
    @criterion_id.setter
    def criterion_id(self, criterion_id: str):
        self._criterion_id = criterion_id

    @property
    def rating_id(self):
        return self._rating_id
    
    @rating_id.setter
    def rating_id(self, rating_id: str):
        self._rating_id = rating_id

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score: float):
        self._score = score

    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, comment: str):
        self._comment = comment

    def __str__(self) -> str:
        assignment_info = []
        assignment_info.append(f"\t\t- Identificador del criteri de la rúbrica: {self._criterion_id}")
        assignment_info.append(f"\t\t- Puntuació: {self._score}")
        if self._comment: assignment_info.append(f"\t\t- Comentari del professor: {self._comment}") 
        return '\n'.join(assignment_info)
    
