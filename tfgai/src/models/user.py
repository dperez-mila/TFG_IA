
class User(object):
    
    def __init__(self, id: str, full_name: str, first_name: str = "", last_name: str = "",
                 visibility: dict = None):
        self._id = id
        self._full_name = full_name
        self._first_name = first_name
        self._last_name = last_name
        self._visibility = visibility

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, full_name: str):
        self._full_name = full_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    def __str__(self) -> str:
        user_info = []
        user_info.append("INFORMACIÓ DE L'USUARI")
        if self._visibility == None or self._visibility["id"] == True:
            user_info.append(f"- Identificador de l'usuari: {self._id}")
        if self._visibility == None or self._visibility["full_name"] == True:
            user_info.append(f"- Nom complert de l'usuari: {self._full_name}")
        if self._visibility == None or self._visibility["first_name"] == True:
            user_info.append(f"- Nom de l'usuari: {self._first_name}")
        if self._visibility == None or self._visibility["last_name"] == True:
            user_info.append(f"- Cognoms de l'usuari: {self._last_name}")
        return '\n'.join(user_info)
     
    