
from .database_service import DataBaseService
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
from ...repositories import SQLite3Repository


class SQLite3Service(DataBaseService):

    def __init__(self, database_path: str):
        self._course_repository = SQLite3Repository(database_path, Course)
        self._assignment_repository = SQLite3Repository(database_path, Assignment)
        self._rubric_repository = SQLite3Repository(database_path, Rubric)
        self._criterion_repository = SQLite3Repository(database_path, Criterion)
        self._rating_repository = SQLite3Repository(database_path, Rating)
        self._association_repository = SQLite3Repository(database_path, Association)
        self._submission_repository = SQLite3Repository(database_path, Submission)
        self._attachment_repository = SQLite3Repository(database_path, Attachment)
        self._assessment_repository = SQLite3Repository(database_path, Assessment)
        self._user_repository = SQLite3Repository(database_path, User)
        self._enrollment_repository = SQLite3Repository(database_path, Enrollment)


    def add_course(self, course: Course):
        self._course_repository.add(course)

    def get_course(self, course_id: str = None, **conditions) -> list[Course]:
        return self._course_repository.get(course_id, **conditions)

    def update_course(self, course_id: str, course: Course):
        self._course_repository.update(course_id, course)

    def delete_course(self, course_id: str):
        self._course_repository.delete(course_id)

    def add_assignment(self, assignment: Assignment):
        self._assignment_repository.add(assignment)

    def get_assignment(self, assignment_id: str = None, **conditions) -> list[Assignment]:
        return self._assignment_repository.get(assignment_id, **conditions)

    def update_assignment(self, assignment_id: str, assignment: Assignment):
        self._assignment_repository.update(assignment_id, assignment)

    def delete_assignment(self, assignment_id: str):
        self._assignment_repository.delete(assignment_id)

    def add_rubric(self, rubric: Rubric):
        self._rubric_repository.add(rubric)

    def get_rubric(self, rubric_id: str = None, **conditions) -> list[Rubric]:
        return self._rubric_repository.get(rubric_id, **conditions)

    def update_rubric(self, rubric_id: str, rubric: Rubric):
        self._rubric_repository.update(rubric_id, rubric)

    def delete_rubric(self, rubric_id: str):
        self._rubric_repository.delete(rubric_id)

    def add_criterion(self, criterion: Criterion):
        self._criterion_repository.add(criterion)

    def get_criterion(self, criterion_id: str = None, **conditions) -> list[Criterion]:
        return self._criterion_repository.get(criterion_id, **conditions)

    def update_criterion(self, criterion_id: str, criterion: Criterion):
        self._criterion_repository.update(criterion_id, criterion)

    def delete_criterion(self, criterion_id: str):
        self._criterion_repository.delete(criterion_id)

    def add_rating(self, rating: Rating):
        self._rating_repository.add(rating)

    def get_rating(self, rating_id: str = None, **conditions) -> list[Rating]:
        return self._rating_repository.get(rating_id, **conditions)

    def update_rating(self, rating_id: str, rating: Rating):
        self._rating_repository.update(rating_id, rating)

    def delete_rating(self, rating_id: str):
        self._rating_repository.delete(rating_id)

    def add_association(self, association: Association):
        self._association_repository.add(association)

    def get_association(self, association_id: str = None, **conditions) -> list[Association]:
        return self._association_repository.get(association_id, **conditions)
    
    def update_association(self, association_id: str, association: Association):
        self._association_repository.update(association_id, association)

    def delete_association(self, association_id: str):
        self._association_repository.delete(association_id)

    def add_submission(self, submission: Submission):
        self._submission_repository.add(submission)

    def get_submission(self, submission_id: str = None, **conditions) -> list[Submission]:
        return self._submission_repository.get(submission_id, **conditions)

    def update_submission(self, submission_id: str, submission: Submission):
        self._submission_repository.update(submission_id, submission)

    def delete_submission(self, submission_id: str):
        self._submission_repository.delete(submission_id)

    def add_attachment(self, attachment: Attachment):
        self._attachment_repository.add(attachment)

    def get_attachment(self, attachment_id: str = None, **conditions) -> list[Attachment]:
        return self._attachment_repository.get(attachment_id, **conditions)

    def update_attachment(self, attachment_id: str, attachment: Attachment):
        self._attachment_repository.update(attachment_id, attachment)

    def delete_attachment(self, attachment_id: str):
        self._attachment_repository.delete(attachment_id)

    def add_assessment(self, assessment: Assessment):
        self._assessment_repository.add(assessment)

    def get_assessment(self, assessment_id: str = None, **conditions) -> list[Assessment]:
        return self._assessment_repository.get(assessment_id, **conditions)

    def update_assessment(self, assessment_id: str, assessment: Assessment):
        self._assessment_repository.update(assessment_id, assessment)

    def delete_assessment(self, assessment_id: str):
        self._assessment_repository.delete(assessment_id)

    def add_user(self, user: User):
        self._user_repository.add(user)

    def get_user(self, user_id: str = None, **conditions) -> list[User]:
        return self._user_repository.get(user_id, **conditions)

    def update_user(self, user_id: str, user: User):
        self._user_repository.update(user_id, user)

    def delete_user(self, user_id: str):
        self._user_repository.delete(user_id)
    
    def add_enrollment(self, enrollment: Enrollment):
        self._enrollment_repository.add(enrollment)

    def get_enrollment(self, enrollment_id: str = None, **conditions) -> list[Enrollment]:
        return self._enrollment_repository.get(enrollment_id, **conditions)
    
    def update_enrollment(self, enrollment_id: str, enrollment: Enrollment):
        self._enrollment_repository.update(enrollment_id, enrollment)

    def delete_enrollment(self, enrollment_id: str):
        self._enrollment_repository.delete(enrollment_id)

