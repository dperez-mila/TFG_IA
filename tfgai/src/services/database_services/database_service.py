
from abc import ABC, abstractmethod

from ...models import (
    Course,
    Assignment,
    Rubric,
    Criterion,
    Rating,
    Association,
    Submission,
    Attachment,
    Assessment,
    User,
    Enrollment
)


class DataBaseService(ABC):
    
    @abstractmethod
    def add_course(self, course: Course):
        pass

    @abstractmethod
    def get_course(self, course_id: str = None, **conditions) -> list[Course]:
        pass

    @abstractmethod
    def update_course(self, course_id: str, course: Course):
        pass

    @abstractmethod
    def delete_course(self, course_id: str):
        pass

    @abstractmethod
    def add_assignment(self, assignment: Assignment):
        pass

    @abstractmethod
    def get_assignment(self, assignment_id: str = None, **conditions) -> list[Assignment]:
        pass

    @abstractmethod
    def update_assignment(self, assignment_id: str, assignment: Assignment):
        pass

    @abstractmethod
    def delete_assignment(self, assignment_id: str):
        pass

    @abstractmethod
    def add_rubric(self, rubric: Rubric):
        pass

    @abstractmethod
    def get_rubric(self, rubric_id: str = None, **conditions) -> list[Rubric]:
        pass

    @abstractmethod
    def update_rubric(self, rubric_id: str, rubric: Rubric):
        pass

    @abstractmethod
    def delete_rubric(self, rubric_id: str):
        pass

    @abstractmethod
    def add_criterion(self, criterion: Criterion):
        pass

    @abstractmethod
    def get_criterion(self, criterion_id: str = None, **conditions) -> list[Criterion]:
        pass

    @abstractmethod
    def update_criterion(self, criterion_id: str, criterion: Criterion):
        pass

    @abstractmethod
    def delete_criterion(self, criterion_id: str):
        pass

    @abstractmethod
    def add_rating(self, rating: Rating):
        pass

    @abstractmethod
    def get_rating(self, rating_id: str = None, **conditions) -> list[Rating]:
        pass

    @abstractmethod
    def update_rating(self, rating_id: str, rating: Rating):
        pass

    @abstractmethod
    def delete_rating(self, rating_id: str):
        pass

    @abstractmethod
    def add_association(self, association: Association):
        pass

    @abstractmethod
    def get_association(self, association_id: str = None, **conditions) -> list[Association]:
        pass

    @abstractmethod
    def update_association(self, association_id: str, association: Association):
        pass

    @abstractmethod
    def delete_association(self, association_id: str):
        pass

    @abstractmethod
    def add_submission(self, submission: Submission):
        pass

    @abstractmethod
    def get_submission(self, submission_id: str = None, **conditions) -> list[Submission]:
        pass

    @abstractmethod
    def update_submission(self, submission_id: str, submission: Submission):
        pass

    @abstractmethod
    def delete_submission(self, submission_id: str):
        pass

    @abstractmethod
    def add_attachment(self, attachment: Attachment):
        pass

    @abstractmethod
    def get_attachment(self, attachment_id: str = None, **conditions) -> list[Attachment]:
        pass

    @abstractmethod
    def update_attachment(self, attachment_id: str, attachment: Attachment):
        pass

    @abstractmethod
    def delete_attachment(self, attachment_id: str):
        pass

    @abstractmethod
    def add_assessment(self, assessment: Assessment):
        pass

    @abstractmethod
    def get_assessment(self, assessment_id: str = None, **conditions) -> list[Assessment]:
        pass

    @abstractmethod
    def update_assessment(self, assessment_id: str, assessment: Assessment):
        pass

    @abstractmethod
    def delete_assessment(self, assessment_id: str):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, user_id: str = None, **conditions) -> list[User]:
        pass

    @abstractmethod
    def update_user(self, user_id: str, user: User):
        pass

    @abstractmethod
    def delete_user(self, user_id: str):
        pass

    @abstractmethod
    def add_enrollment(self, enrollment: Enrollment):
        pass

    @abstractmethod
    def get_enrollment(self, enrollment_id: str = None, **conditions) -> list[Enrollment]:
        pass

    @abstractmethod
    def update_enrollment(self, enrollment_id: str, enrollment: Enrollment):
        pass

    @abstractmethod
    def delete_enrollment(self, enrollment_id: str):
        pass

