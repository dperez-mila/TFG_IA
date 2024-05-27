
from .rating import Rating

class Criterion():

    def __init__(self, id: str, rubric_id: str, description: str, long_description: str, 
                 max_score: float, ratings: list[Rating] = [], visibility: dict = None):
        self._id = id
        self._rubric_id = rubric_id
        self._description = description
        self._long_description = long_description
        self._max_score = max_score
        self._ratings = ratings
        self._visibility = visibility

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def rubric_id(self) -> str:
        return self._rubric_id

    @rubric_id.setter
    def rubric_id(self, rubric_id: str):
        self._rubric_id = rubric_id 
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def long_description(self) -> str:
        return self._long_description
    
    @long_description.setter
    def long_description(self, long_description: str):
        self._long_description = long_description

    @property
    def max_score(self) -> float:
        return self._max_score
    
    @max_score.setter 
    def max_score(self, max_score: float):
        self._max_score = max_score
    
    @property
    def ratings(self) -> list[Rating]:
        return self._ratings
    
    @ratings.setter
    def ratings(self, ratings: list[Rating]):
        self._ratings = ratings
        
    def __str__(self) -> str:
        criterion_info = []
        criterion_info.append(f"\t\t- Identificador del criteri: {self._id}")
        criterion_info.append(f"\t\t- Descripció del criteri: {self._description}")
        criterion_info.append(f"\t\t- Descripció llarga del criteri: {self._long_description}")
        criterion_info.append(f"\t\t- Puntuació màxima del criteri: {self._max_score}")
        criterion_info.append(f"\t\t- Classificacions del criteri:")
        for rating in self._ratings:
            criterion_info.append(str(rating))
        return '\n'.join(criterion_info)
    
    #def get_rating(self, rating_id):
    #    for rating in self._ratings:
    #        if rating.id == rating_id:
    #            return rating
    #    return None
