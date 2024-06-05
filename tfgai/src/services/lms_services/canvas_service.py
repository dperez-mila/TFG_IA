
import logging

from . import LMSService
from ...clients import CanvasClient
from ...enums import EnrollmentType
from ...models import (
    Model,
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


class CanvasService(LMSService):

    _model_mapping: dict = {
        'course': (Course, {'id': 'id', 'name': 'name', 'locale': 'language'}),
        'assignment': (Assignment, {'id': 'id', 'name': 'name', 'description': 'description', 
                                    'points_possible': 'max_score'}),
        'rubric': (Rubric, {'id': 'id', 'title': 'title', 'points_possible': 'max_score'}),
        'criterion': (Criterion, {'id': 'id', 'description': 'description', 
                                  'long_description': 'long_description', 'points': 'max_score'}),
        'rating': (Rating, {'description': 'description', 'long_description': 'long_description',
                            'points': 'max_score'}),
        'association': (Association, {'id': 'id', 'rubric_id': 'rubric_id', 
                                      'association_id': 'associated_object_key'}),
        'submission': (Submission, {'id': 'id', 'score': 'score', 'late': 'late', 'user_id': 'user_id'}),
        'attachment': (Attachment, {'id': 'id', 'filename': 'file_name', 'mime_class': 'file_extension',
                                    'size': 'file_size', 'url': 'file_url'}),
        'assessment': (Assessment, {'id': 'id', 'criterion_id': 'criterion_id', 'points': 'score',
                                    'comments': 'comments'}),
        'user': (User, {'id': 'id', 'login_id': 'username', 'email': 'email', 'name': 'full_name',
                        'first_name': 'first_name', 'last_name': 'last_name'}),
        'enrollment': (Enrollment, {'id': 'id', 'course_id': 'course_id', 'user_id': 'user_id'})
    }

    def __init__(self, base_url: str, token: str):
        self._lms_client = CanvasClient(base_url, token)
    
    def _create_model(self, model_name: str, data: dict, **params) -> Model:
        model_info : tuple[Model, dict] = self._model_mapping.get(model_name)
        if not model_info:
            raise ValueError(f"Unknown model: {model_name}")

        model_class, key_mapping = model_info

        translated_data : dict = {
            model_attr: data[dict_key] 
            for dict_key, model_attr in key_mapping.items() if dict_key in data
        }
        
        return model_class(**translated_data, **params)

    def _map_course(self, course_data: dict, **params) -> Course:
        course: Course = self._create_model('course', course_data, **params)
        return course
    
    def _map_assignment(self, assignment_data: dict, **params) -> Assignment:
        assignment: Assignment = self._create_model('assignment', assignment_data, **params)

        rubric_params: dict = {'course_id': assignment.course_id, 'assignment_id': assignment.id}
        rubric: Rubric = self._map_rubric(
            { 'data': assignment_data['rubric'], **assignment_data['rubric_settings']},
            **rubric_params
        )
        assignment.rubric = rubric

        return assignment
        
    def _map_rubric(self, rubric_data: dict, **params) -> Rubric:
        rubric: Rubric = self._create_model('rubric', rubric_data, **params)

        criterion_params: dict = {'rubric_id': rubric.id}
        rubric.criterions = [self._map_criterion(criterion_data, **criterion_params) 
                             for criterion_data in rubric_data['data']]
        
        if rubric_data.get('associations', ''):
            rubric.associations = [self._map_association(association_data)
                                for association_data in rubric_data['associations']]
        
        return rubric

    def _map_criterion(self, criterion_data: dict, **params) -> Criterion:
        criterion: Criterion = self._create_model('criterion', criterion_data, **params)

        rating_params: dict = {'id': f'{criterion.id}_', 'criterion_id': criterion.id}
        for rating_data in criterion_data['ratings']:
            rating_params: dict = {'id': f'{criterion.id}_{rating_data.get("id")}', 
                                   'criterion_id': criterion.id}
            criterion.ratings.append(self._map_rating(rating_data, **rating_params))

        return criterion
    
    def _map_rating(self, rating_data: dict, **params) -> Rating:
        rating: Rating = self._create_model('rating', rating_data, **params)
        return rating
    
    def _map_association(self, association_data: dict, **params) -> Association:
        association_type: dict = {
            'Course': Course,
            'Assignment': Assignment
        }
        _type: Model = association_type.get(association_data['association_type'])
        params: dict = {'associated_object_type': _type}
        association: Association = self._create_model('association', association_data, **params)
        return association
    
    def _map_submission(self, submission_data: dict, **params) -> Submission:
        
        submission: Submission = self._create_model('submission', submission_data, **params)

        attachment_params: dict = {'submission_id': submission.id}
        if submission_data.get('attachments', ''):
            submission.attachment = self._map_attachment(submission_data['attachments'][0], 
                                                        **attachment_params)
        
        if submission_data.get('full_rubric_assessment'):
            submission.rubric_score = submission_data['full_rubric_assessment']['score']
            
            rubric_id: str = submission_data['full_rubric_assessment']['rubric_id']
            association_id: str = submission_data['full_rubric_assessment']['rubric_association']['id']
            for assessment_data in submission_data['full_rubric_assessment']['data']:
                criterion_id = assessment_data['criterion_id']
                assessment_params: dict = {'submission_id': submission.id, 'rubric_id': rubric_id,
                                        'rating_id': f"{criterion_id}_{assessment_data['id']}",
                                        'association_id': association_id}
                submission.assessments.append(self._map_assessment(assessment_data,
                                                                   **assessment_params)) 

        return submission
    
    def _map_assessment(self, assessment_data: dict, **params) -> Assessment:
        assessment: Assessment = self._create_model('assessment', assessment_data, **params)
        return assessment

    def _map_attachment(self, attachment_data: dict, **params) -> Attachment:
        attachment: Attachment = self._create_model('attachment', attachment_data, **params)
        return attachment
    
    def _map_user(self, user_data: dict, **params) -> User:
        user: User = self._create_model('user', user_data, **params)

        for enrollment_data in user_data['enrollments']:
            _type = (EnrollmentType.TEACHER if enrollment_data['type'] == 'TeacherEnrollment' 
                     else EnrollmentType.STUDENT)
            enrollment_params: dict = {'type': _type}
            user.enrollments.append(self._map_enrollment(enrollment_data, **enrollment_params))

        return user
    
    def _map_enrollment(self, enrollment_data: dict, **params) -> Enrollment:
        enrollment: Enrollment = self._create_model('enrollment', enrollment_data, **params)
        return enrollment

    def get_courses(self, course_id: str = None) -> list[Course]:
        data: list[dict] = self._lms_client.get_courses(course_id)
        courses: list[Course] = [self._map_course(course_data) for course_data in data]

        return courses
    
    def get_assignments(self, course_id: str, assignment_id: str = None) -> list[Assignment]:
        data: list[dict] = self._lms_client.get_assignments(course_id, assignment_id)
        params: dict = {'course_id': course_id}
        assignments: list[Assignment] = [self._map_assignment(assignment_data, **params) 
                            for assignment_data in data if assignment_data.get("rubric")]

        return assignments
    
    def get_rubrics(self, course_id: str, assignment_id: str, rubric_id: str = None) -> list[Rubric]:
        data: list[dict] = self._lms_client.get_rubrics(course_id, rubric_id)
        params: dict = {'course_id': course_id, 'assignment_id': assignment_id}
        rubrics: list[Rubric] = [self._map_rubric(rubric_data, **params) for rubric_data in data]

        return rubrics
    
    def get_submissions(self, course_id: str, assignment_id: str, 
                        user_id: str = None) -> list[Submission]:
        data: list[dict] = self._lms_client.get_submissions(course_id, assignment_id, user_id)
        params: dict = {'course_id': course_id, 'assignment_id': assignment_id}
        submissions: list[Submission] = [self._map_submission(submission_data, **params) 
                                         for submission_data in data]
        
        return submissions
    
    # No permissions to issue this method (!)
    def get_attachments(self, attachment_id: str = None) -> list[Attachment]:
        data = self._lms_client.get_attachments(attachment_id)
        attachments = [self._create_model('attachment', attachment_data) for attachment_data in data]
        return attachments
    
    def get_users(self, course_id: str, user_id: str = None) -> list[User]:
        data = self._lms_client.get_users(course_id, user_id)
        users = [self._map_user(user_data) for user_data in data]
        return users
    
    def put_submission_comment(self, course_id: str, assignment_id: str, user_id: str, comment: str):
        self._lms_client.put_submission_comment(course_id, assignment_id, user_id, comment)

    def put_rubric_assessment_comment(self, course_id: str, rubric_association_id: str,
                                      rubric_assessment_id: str, user_id: str, criterion_id: str,
                                      comment: str):
        self._lms_client.put_rubric_assessment_comment(course_id, rubric_association_id, 
                                                       rubric_assessment_id, user_id, criterion_id, 
                                                       comment)

