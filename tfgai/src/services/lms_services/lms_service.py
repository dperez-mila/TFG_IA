
from abc import ABC, abstractmethod
from ...clients import LMSClient
from ...models import Course, Rubric, Assignment, Submission, Attachment


class LMSService(ABC):

    def __init__(self, base_url, token):
        self._lms_client = LMSClient(base_url, token)

    @abstractmethod
    def get_courses(self) -> list[Course]:
        pass

    @abstractmethod
    def get_course(self, course_id) -> Course:
        pass

    @abstractmethod
    def get_rubrics(self, course_id) -> list[Rubric]:
        pass

    @abstractmethod
    def get_rubric(self, course_id, rubric_id) -> Rubric:
        pass

    @abstractmethod
    def get_assignments(self, course_id) -> list[Assignment]:
        pass

    @abstractmethod
    def get_assignment(self, course_id, assignment_id) -> Assignment:
        pass

    @abstractmethod
    def get_submissions(self, course_id, assignment_id) -> list[Submission]:
        pass

    @abstractmethod
    def get_submission(self, course_id: str, assignment_id: str, user_id: str) -> Submission:
        pass

