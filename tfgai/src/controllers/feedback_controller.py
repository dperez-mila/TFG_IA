
from ..services.service_manager import ServiceManager

class FeedbackController():

    def __init__(self, service_manager: ServiceManager):
        self._service_manager = service_manager
    
    def get_data(self, course_id: str, assignment_id: str, user_id: str):
        course = self._service_manager._get_course_data(course_id)
        assignment = self._service_manager._get_assignment_data(assignment_id)
        rubric = self._service_manager._get_rubric_data(assignment.rubric_id)
        submission = self._service_manager._get_submission_data(assignment_id, user_id)
        return course, assignment, rubric, submission
    
    def refresh_data(self, course_id: str, assignment_id: str = None, user_id: str = None):
        self._service_manager.refresh_course_data(course_id)
        if assignment_id:
            self._service_manager.refresh_assignment_data(course_id, assignment_id)
            self._service_manager.refresh_rubric_data(course_id, assignment_id)
        if assignment_id and user_id:
            self._service_manager.refresh_submission_data(course_id, assignment_id, user_id)
    
    def clear_prompt(self):
        self._service_manager.clear_prompt()

    def generate_prompt(self, course_id: str, assignment_id: str, user_id: str):
        self._service_manager.build_prompt(course_id, assignment_id, user_id)

    def generate_response(self):
        self._service_manager.generate_response()

    def generate_feedback(self, course_id: str, assignment_id: str, user_id: str):
        self.generate_prompt(course_id, assignment_id, user_id)
        self.generate_response()

    def publish_feedback(self, course_id: str, assignment_id: str, user_id: str):
        pass

