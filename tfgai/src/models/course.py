
class Course():

    def __init__(self, id: str, name: str, language: str, assignments: list[str] = [],
                 visibility: dict = None):
        self._id = id
        self._name = name
        self._language = language
        self._assignments = assignments
        self._visibility = visibility

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = str(id)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = str(name)

    @property
    def language(self) -> str:
        return self._language
    
    @language.setter
    def language(self, language: str):
        self._name = str(language)

    @property
    def assignments(self) -> list[str]:
        return self._assignments
    
    @assignments.setter
    def assignments(self, assignments: list[str]):
        self._assignments = assignments

    def __str__(self) -> str:
        course_info = []
        course_info.append("Informació de l'assignatura:")
        course_info.append(f"\t- Nom de l'assignatura: {self._name}")
        course_info.append(f"\t- Idioma: català")
        return '\n'.join(course_info)
    
    