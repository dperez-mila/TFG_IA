
from abc import ABC, abstractmethod
from ...clients import LMSClient
from ...models import Course, Rubric, Assignment, Submission, Attachment, User


class LMSService(ABC):

    def __init__(self, base_url, token):
        self._lms_client = LMSClient(base_url, token)

    @abstractmethod
    def get_courses(self, course_id: str = None) -> list[Course]:
        pass
    
    @abstractmethod
    def get_assignments(self, course_id: str, assignment_id: str = None) -> list[Assignment]:
        pass
    
    @abstractmethod
    def get_rubrics(self, course_id: str, assignment_id: str, rubric_id: str = None) -> list[Rubric]:
        pass
    
    @abstractmethod
    def get_submissions(self, course_id: str, assignment_id: str, 
                        user_id: str = None) -> list[Submission]:
        pass
    
    @abstractmethod
    def get_attachments(self, attachment_id: str = None) -> list[Attachment]:
        pass
    
    @abstractmethod
    def get_users(self, course_id: str, user_id: str = None) -> list[User]:
        pass
    
    @abstractmethod
    def put_submission_comment(self, course_id: str, assignment_id: str, user_id: str, comment: str):
        pass

    @abstractmethod
    def put_rubric_assessment_comment(self, course_id: str, rubric_association_id: str,
                                      rubric_assessment_id: str, user_id: str, criterion_id: str,
                                      comment: str):
        pass

