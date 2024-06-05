
from ..services.service_manager import ServiceManager
from ..models import Course, Attachment


class FeedbackController():

    def __init__(self, service_manager: ServiceManager):
        self._service_manager = service_manager
        self.data = self.get_data()
    
    def add_data(self, course_id: str = None, assignment_id: str = None, user_id: str = None):
        self._service_manager.add_data(course_id, assignment_id, user_id)

    def get_data(self, course_id: str = None, assignment_id: str = None, user_id: str = None):
        data = self._service_manager.get_data(course_id, assignment_id, user_id)
        return data

    def update_data(self, data: list[Course]):
        pass

    def delete_data(self):
        pass
    
    def get_attachment_content(self, attachment: Attachment, filters: list[str] = []) -> str:
        attachment_content = self._service_manager.get_attachment_content(attachment, filters)
        return attachment_content
    
    def get_external_file_content(self, filters: list[str] = []):
        external_content = self._service_manager.get_external_file_content()
        return external_content

    def clear_prompt(self):
        self._service_manager.clear_prompt()

    def generate_prompt(self, **data_content):
        self._service_manager.build_prompt(**data_content)

    def generate_response(self, **options):
        self._service_manager.generate_response(**options)

    def generate_feedback(self, **data_content):
        self.generate_prompt(**data_content)
        self.generate_response()

    def publish_feedback(self, course_id: str, assignment_id: str, user_id: str):
        pass

