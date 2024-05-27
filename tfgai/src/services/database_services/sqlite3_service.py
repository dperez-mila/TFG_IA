
from . import DataManagementService
from ...database import SQLiteDataManagement
from ...repositories import (
    CourseRepository, 
    AssignmentRepository, 
    RubricRepository, 
    CriterionRepository,
    RatingRepository,
    SubmissionRepository,
    AttachmentRepository,
    AssessmentRepository
)
from ...models import Course, Assignment, Rubric, Submission


class SQLiteService(DataManagementService):
    
    def __init__(self, db_path: str):
        self._sqlite_db = SQLiteDataManagement(db_path)
        with self._sqlite_db as db:
            self._course_repository = CourseRepository(db)
            self._assignment_repository = AssignmentRepository(db)
            self._rubric_repository = RubricRepository(db)
            self._criterion_repository = CriterionRepository(db)
            self._rating_repository = RatingRepository(db)
            self._submission_repository = SubmissionRepository(db)
            self._attachment_repository = AttachmentRepository(db)
            self._assessment_repository = AssessmentRepository(db)

    def get_course(self, course_id: str) -> Course:
        with self._sqlite_db:
            course = self._course_repository.get(course_id)
        return course
    
    def add_course(self, course: Course):
        with self._sqlite_db:
            self._course_repository.add(course)

    def update_course(self, course: Course):
        with self._sqlite_db:
            self._course_repository.update(course)
    
    def get_assignment(self, assignment_id: str) -> Assignment:
        with self._sqlite_db:
            assignment = self._assignment_repository.get(assignment_id)
        return assignment
    
    def add_assignment(self, assignment: Assignment):
        with self._sqlite_db:
            self._assignment_repository.add(assignment)

    def update_assignment(self, assignment: Assignment):
        with self._sqlite_db:
            self._assignment_repository.update(assignment)

    def get_rubric(self, rubric_id: str) -> Rubric:
        with self._sqlite_db:
            rubric = self._rubric_repository.get(rubric_id)
            if rubric:
                criteria = self._criterion_repository.get_by_rubric(rubric_id)
                rubric_criteria = []
                for criterion in criteria:
                    ratings = self._rating_repository.get_by_criterion(criterion.id)
                    criterion.ratings = ratings
                    rubric_criteria.append(criterion)
                rubric.criteria = rubric_criteria
                return rubric
            else:
                return None
        
    
    def add_rubric(self, rubric: Rubric):
        with self._sqlite_db:
            self._rubric_repository.add(rubric)
            for criterion in rubric.criteria:
                self._criterion_repository.add(criterion)
                for rating in criterion.ratings:
                    self._rating_repository.add(rating)

    def update_rubric(self, rubric: Rubric):
        with self._sqlite_db:
            self._rubric_repository.update(rubric)
            for criterion in rubric.criteria:
                self._criterion_repository.update(criterion)
                for rating in criterion.ratings:
                    self._rating_repository.update(rating)

    def get_submission(self, assignment_id: str, user_id: str) -> Submission:
        with self._sqlite_db:
            submissions = self._submission_repository.get_by_assignment_user(assignment_id, user_id)
            if submissions:
                submission = submissions[0]
                attachment = self._attachment_repository.get_by_submission(submission.id)[-1]
                assessments = self._assessment_repository.get_by_submission(submission.id)
                submission.attachment = attachment
                submission.assessments = assessments
                return submission
            else:
                return None

    def add_submission(self, submission: Submission):
        with self._sqlite_db:
            self._submission_repository.add(submission)
            self._attachment_repository.add(submission.attachment)
            for assessment in submission.assessments:
                self._assessment_repository.add(assessment)

    def update_submission(self, submission: Submission):
        with self._sqlite_db:
            self._submission_repository.update(submission)
            self._attachment_repository.update(submission.attachment)
            for assessment in submission.assessments:
                self._assessment_repository.update(assessment)

