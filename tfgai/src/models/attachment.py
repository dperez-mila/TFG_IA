
class Attachment():

    def __init__(self, id: str, submission_id: str, file_name: str, url: str, type: str, size: float,
                 visibility: dict = None):
        self._id = id
        self._submission_id = submission_id
        self._file_name = file_name
        self._url = url
        self._type = type
        self._size = size
        self._visibility = visibility

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def submission_id(self) -> str:
        return self._submission_id
    
    @submission_id.setter
    def submission_id(self, submission_id: str):
        self._submission_id = submission_id

    @property
    def file_name(self) -> str:
        return self._file_name
    
    @file_name.setter
    def file_name(self, file_name: str):
        self._file_name = file_name

    @property
    def url(self) -> str:
        return self._url
    
    @url.setter
    def url(self, url: str):
        self._url = url

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def size(self) -> float:
        return self._size
    
    @size.setter
    def size(self, size: float):
        self._size = size

