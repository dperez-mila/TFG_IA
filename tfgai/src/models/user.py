
class User(object):
    
    def __init__(self, id: str, full_name: str, first_name: str = "", last_name: str = "",
                 username: str = "", email: str = ""):
        self._id = id
        self._full_name = full_name
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def full_name(self) -> str:
        return self._full_name
    
    @full_name.setter
    def full_name(self, full_name: str):
        self._full_name = full_name

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        self._email = email
     
    