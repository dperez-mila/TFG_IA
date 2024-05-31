
from tkinter import Tk, filedialog
from ..services.service_manager import ServiceManager
from ..models import Course, Assignment, Rubric, Submission, Attachment, User
from ..utils import pdf_content_from_file_path

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
    
    def get_attachment_content(self, attachment: Attachment, student: User = None, 
                               teacher: User = None) -> str:
        attachment_content = self._service_manager.get_attachment_content(attachment)
        filters = []
        if student:
            filters += [student.full_name, student.first_name, student.last_name, student.email]
        if teacher:
            filters += [teacher.full_name, teacher.first_name, teacher.last_name, teacher.email]
        if len(filters) > 0:
            attachment_content = self.filter_out_content(attachment_content, filters)
        return attachment_content
    
    def get_assessed_rubric(self, rubric: Rubric, submission: Submission) -> Rubric:
        return self._service_manager.get_assessed_rubric_data(rubric, submission)
    
    def get_user(self, course_id: str, user_id: str) -> User:
        return self._service_manager.get_user(course_id, user_id)
    
    def get_external_content(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Select an external PDF file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            content = pdf_content_from_file_path(file_path)
            return content
        return None
            
    def refresh_data(self, course_id: str, assignment_id: str = None, user_id: str = None):
        self._service_manager.refresh_course_data(course_id)
        if assignment_id:
            self._service_manager.refresh_assignment_data(course_id, assignment_id)
            self._service_manager.refresh_rubric_data(course_id, assignment_id)
        if assignment_id and user_id:
            self._service_manager.refresh_submission_data(course_id, assignment_id, user_id)
    
    def filter_out_content(self, content: str, filters: list[str]) -> str:
        filtered_content = content
        for filter in filters:
            filtered_content = filtered_content.replace(filter, "")
        return filtered_content

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

