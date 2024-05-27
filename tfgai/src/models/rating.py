
class Rating():

    def __init__(self, id: str, criterion_id: str, description: str, long_description: str, 
                 max_score: float, visibility: dict = None):
        self._id = id
        self._criterion_id = criterion_id
        self._description = description
        self._long_description = long_description
        self._max_score = max_score
        self._comment = ""
        self._visibility = visibility

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def criterion_id(self):
        return self._criterion_id
    
    @criterion_id.setter
    def criterion_id(self, criterion_id: str):
        self._criterion_id = criterion_id

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description: str):
        self._description = description
    
    @property
    def long_description(self):
        return self._long_description
    
    @long_description.setter
    def long_description(self, long_description: str):
        self._long_description = long_description

    @property
    def max_score(self):
        return self._max_score
    
    @max_score.setter
    def max_score(self, max_score: float):
        self._max_score = max_score

    @property
    def comment(self) -> str:
        return self._comment
    
    @comment.setter
    def comment(self, comment: str):
        self._comment = comment

    def __str__(self) -> str:
        rating_info = []
        rating_info.append(f"\t\t\t- Descripció de la classificació: {self._description}")
        rating_info.append(f"\t\t\t- Descripció llarga de la classificació: {self._long_description}")
        rating_info.append(f"\t\t\t- Màxima puntuació de la classificació: {self._max_score}")
        return '\n'.join(rating_info)
    