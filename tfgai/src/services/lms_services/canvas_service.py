
from ...models import (
    Course,
    Assignment, 
    Rubric, 
    Criterion, 
    Rating,
    Submission, 
    Attachment, 
    Assessment
)
from . import LMSService
from ...clients import CanvasClient


class CanvasService(LMSService):

    def __init__(self, base_url, token):
        self._lms_client = CanvasClient(base_url, token)

    def _course_mapper(self, course_dict: dict) -> Course:
        return Course(course_dict['id'], course_dict['name'], course_dict['locale'])
    
    def _assignment_mapper(self, assignment_dict: dict) -> Assignment:
        if 'rubric_settings' not in assignment_dict:
            raise KeyError("The assignment must contain a rubric!")
        return Assignment(assignment_dict['id'], assignment_dict['course_id'], 
                          assignment_dict['rubric_settings']['id'], assignment_dict['name'], 
                          assignment_dict['description'], assignment_dict['points_possible'])
    
    def _rubric_mapper(self, rubric_dict: dict) -> Rubric:
        rubric_id = rubric_dict['id']
        rubric_criteria = []
        for criterion_dict in rubric_dict['data']:
            ratings = []
            ratings.extend(self._rating_mapper(criterion_dict['id'], rating) 
                           for rating in criterion_dict['ratings'])
            criterion = self._criterion_mapper(rubric_id, criterion_dict, ratings) 
            rubric_criteria.append(criterion)    
        return Rubric(rubric_dict['id'], rubric_dict['context_id'], rubric_dict['title'], 
                      rubric_dict['points_possible'], rubric_criteria)
            
    def _criterion_mapper(self, rubric_id: str, criterion_dict: dict, 
                          ratings: list[Rating]) -> Criterion:
        return Criterion(criterion_dict['id'], rubric_id, criterion_dict['description'], 
                         criterion_dict['long_description'], criterion_dict['points'], ratings)
    
    def _rating_mapper(self, criterion_id: str, rating_dict: dict) -> Rating:
        return Rating(rating_dict['id'], criterion_id, rating_dict['description'], 
                      rating_dict['long_description'], rating_dict['points'])

    def _submission_mapper(self, rubric_id: str, submission_dict: dict) -> Submission:
        submission_id = submission_dict['id']
        attachment = self._attachment_mapper(submission_id, submission_dict['attachments'][-1]) 
        assessments = [self._assessment_mapper(submission_id, rubric_id, assessment_dict)
                       for assessment_dict in submission_dict['full_rubric_assessment']['data']]
        return Submission(submission_id, submission_dict['assignment_id'], submission_dict['user_id'],
                          submission_dict['grader_id'], submission_dict['score'], submission_dict['late'], attachment, assessments)

    def _attachment_mapper(self, submission_id: str, attachment_dict: dict) -> Attachment:
        return Attachment(attachment_dict['id'], submission_id, attachment_dict['filename'], attachment_dict['url'], attachment_dict['mime_class'], attachment_dict['size'])
    
    def _assessment_mapper(self, submission_id: str, rubric_id: str, 
                           assessment_dict: dict) -> Assessment:
        criterion_id = assessment_dict['criterion_id']
        rating_id = assessment_dict['id']
        return Assessment(assessment_dict['id'], submission_id, rubric_id, criterion_id, rating_id,assessment_dict['points'], assessment_dict['comments'])
    
    def get_courses(self) -> list[Course]:
        courses_dict_list = self._lms_client.get_courses()
        courses = [self._course_mapper(course_dict) for course_dict in courses_dict_list]
        return courses
    
    def get_course(self, course_id) -> Course:
        course_dict = self._lms_client.get_course(course_id)
        return self._course_mapper(course_dict)
    
    def get_rubrics(self, course_id) -> list[Rubric]:
        rubrics_dict_list = self._lms_client.get_rubrics(course_id)
        rubrics = [self._rubric_mapper(rubric_dict) for rubric_dict in rubrics_dict_list]
        return rubrics
    
    def get_rubric(self, course_id, rubric_id) -> Rubric:
        rubric_dict = self._lms_client.get_rubric(course_id, rubric_id)
        return self._rubric_mapper(rubric_dict)
    
    def get_assignments(self, course_id) -> list[Assignment]:
        assignments_dict_list = self._lms_client.get_assignments(course_id)
        assignments = [self._assignment_mapper(assignment_dict) 
                       for assignment_dict in assignments_dict_list]
        return assignments
    
    def get_assignment(self, course_id, assignment_id) -> Assignment:
        assignment_dict = self._lms_client.get_assignment(course_id, assignment_id)
        return self._assignment_mapper(assignment_dict)
    
    def get_submissions(self, course_id, assignment_id) -> list[Submission]:
        submissions_dict_list = self._lms_client.get_submissions(course_id, assignment_id)
        submissions = [self._submission_mapper(submission_dict) 
                           for submission_dict in submissions_dict_list]
        return submissions
    
    def get_submission(self, course_id: str, assignment_id: str, user_id: str) -> Submission:
        submission_dict = self._lms_client.get_submission(course_id, assignment_id, user_id)
        rubric_id = submission_dict['full_rubric_assessment']['rubric_id']
        return self._submission_mapper(rubric_id, submission_dict)

