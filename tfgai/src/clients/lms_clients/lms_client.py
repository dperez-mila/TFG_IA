
from abc import ABC, abstractmethod
import requests


class LMSClient(ABC):

    def __init__(self, base_url, token):
        self._base_url = base_url
        self._token = token
        self._headers = {
            'Authorization': 'Bearer ' + self._token,
            'Content-Type': 'application/json'
        }

    def _get(self, endpoint: str, params: tuple = None):
        url = f"{self._base_url}/{endpoint}"
        response = requests.get(url, headers=self._headers, params=params)
        response.raise_for_status()
        return response.json()

    @abstractmethod
    def get_courses(self):
        pass

    @abstractmethod
    def get_course(self, course_id: str):
        pass

    @abstractmethod
    def get_user(self, course_id: str, user_id: str):
        pass

    @abstractmethod
    def get_rubrics(self, course_id: str):
        pass
    
    @abstractmethod
    def get_rubric(self, course_id: str, rubric_id: str):
        pass
    
    @abstractmethod
    def get_assignments(self, course_id: str):
        pass

    @abstractmethod
    def get_assignment(self, course_id: str, assignment_id: str):
        pass

    @abstractmethod
    def get_submissions(self, course_id: str, assignment_id: str):
        pass

    @abstractmethod
    def get_submission(self, course_id: str, assignment_id: str, user_id: str):
        pass

    @abstractmethod
    def put_submission_comment(self, course_id: str, assignment_id: str, user_id: str, comment: str):
        pass

