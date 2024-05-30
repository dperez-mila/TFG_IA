
from ..services.service_manager import ServiceManager
from ..models import Course, Assignment, Rubric, Submission, Attachment

class FeedbackController():

    def __init__(self, service_manager: ServiceManager):
        self._service_manager = service_manager
    
    def get_course(self, course_id: str) -> Course:
        return self._service_manager.get_course_data(course_id)
    
    def get_assignment(self, assignment_id: str) -> Assignment:
        return self._service_manager.get_assignment_data(assignment_id)
    
    def get_rubric(self, rubric_id: str) -> Rubric:
        return self._service_manager.get_rubric_data(rubric_id)
    
    def get_submission(self, assignment_id: str, user_id: str) -> Submission:
        return self._service_manager.get_submission_data(assignment_id, user_id)
    
    def get_attachment_content(self, attachment: Attachment) -> str:
        return self._service_manager.get_attachment_content(attachment)
    
    def get_assessed_rubric(self, rubric: Rubric, submission: Submission) -> Rubric:
        return self._service_manager.get_assessed_rubric_data(rubric, submission)
    
    def refresh_data(self, course_id: str, assignment_id: str = None, user_id: str = None):
        self._service_manager.refresh_course_data(course_id)
        if assignment_id:
            self._service_manager.refresh_assignment_data(course_id, assignment_id)
            self._service_manager.refresh_rubric_data(course_id, assignment_id)
        if assignment_id and user_id:
            self._service_manager.refresh_submission_data(course_id, assignment_id, user_id)
    
    def clear_prompt(self):
        self._service_manager.clear_prompt()

    def generate_prompt(self, **data_content):
        self._service_manager.build_prompt(**data_content)

    def generate_response(self):
        self._service_manager.generate_response()

    def generate_feedback(self, **data_content):
        self.generate_prompt(data_content)
        self.generate_response()

    def publish_feedback(self, course_id: str, assignment_id: str, user_id: str):
        pass

