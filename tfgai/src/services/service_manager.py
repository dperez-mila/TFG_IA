
from jinja2 import Template
from tkinter import Tk, filedialog

from .llm_services import LLMService
from .lms_services import LMSService
from .database_services import DataBaseService
from ..models import Course, Rubric, Submission, Assignment, Attachment, User, Enrollment
from ..enums import FileExtension
from ..utils import load_json_file, dump_json_file, clear_json_file
from ..utils import pdf_content_from_url, pdf_content_from_file_path
from ..utils import read_txt_file, write_txt_file
from ..core import PROMPT_TEMPLATE_FILEPATH, PROMPT_FILEPATH, RESPONSE_FILEPATH


class ServiceManager():

    def __init__(self, llm_service: LLMService, lms_service: LMSService, db_service: DataBaseService):
        self._llm_service: LLMService = llm_service
        self._lms_service: LMSService = lms_service
        self._db_service: DataBaseService = db_service

    def _retrieve_data(self, course_id: str = None, assignment_id: str = None, user_id: str = None
                       ) -> list[Course]:
        courses: list[Course] = self._lms_service.get_courses(course_id)

        for course in courses:
            users: list[User] = self._lms_service.get_users(course.id, user_id)
            course.users = users

            assignments: list[Assignment] = self._lms_service.get_assignments(course.id, assignment_id)
            course.assignments = assignments

            for assignment in assignments:
                if assignment.rubric:
                    rubric: Rubric = self._lms_service.get_rubrics(course.id, assignment.id, 
                                                                assignment.rubric.id)[0]
                    assignment.rubric = rubric
                    course.rubrics.append(rubric)

                submissions: list[Submission] = self._lms_service.get_submissions(course.id, 
                                                                                  assignment.id, user_id)
                assignment.submissions = submissions

        return courses

    def filter_out_content(self, content: str, filters: list[str]) -> str:
        filtered_content = content
        for _filter in filters:
            filtered_content = filtered_content.replace(_filter, "")
        return filtered_content

    def add_message(self, content: str, role: str = "user"): #OK
        messages = load_json_file(PROMPT_FILEPATH)
        messages.append({"role": role, "content": content})
        dump_json_file(PROMPT_FILEPATH, messages)

    def add_data(self, course_id: str = None, assignment_id: str = None, user_id: str = None):
        courses: list[Course] = self._retrieve_data(course_id, assignment_id, user_id)
        for course in courses:
            if not self._db_service.get_course(course.id):
                self._db_service.add_course(course)

                for rubric in course.rubrics:
                    if not self._db_service.get_rubric(rubric.id):
                        self._db_service.add_rubric(rubric)
                        for criterion in rubric.criterions:
                            self._db_service.add_criterion(criterion)
                            for rating in criterion.ratings:
                                self._db_service.add_rating(rating)
                        for association in rubric.associations:
                            self._db_service.add_association(association)

                for assignment in course.assignments:
                    if not self._db_service.get_assignment(assignment.id):
                        self._db_service.add_assignment(assignment)

                        for submission in assignment.submissions:
                            if not self._db_service.get_submission(submission.id):
                                self._db_service.add_submission(submission)
                                if submission.attachment:
                                    self._db_service.add_attachment(submission.attachment)
                                for assessment in submission.assessments:
                                    self._db_service.add_assessment(assessment)

                for user in course.users:
                    if not self._db_service.get_user(user.id):
                        self._db_service.add_user(user)
                        for enrollment in user.enrollments:
                            self._db_service.add_enrollment(enrollment)
    
    def get_data(self, course_id: str = None, assignment_id: str = None, user_id: str = None):
        courses: list[Course] = self._db_service.get_course(course_id)
        for course in courses:
            course.assignments = self._db_service.get_assignment(assignment_id)
            for assignment in course.assignments:
                rubrics: list[Rubric] = self._db_service.get_rubric(course_id = course.id, 
                                                            assignment_id = assignment.id)
                for rubric in rubrics:
                    rubric.associations = self._db_service.get_association(rubric_id = rubric.id)

                    rubric.criterions = self._db_service.get_criterion(rubric_id = rubric.id)
                    for criterion in rubric.criterions:
                        criterion.ratings = self._db_service.get_rating(
                            criterion_id = criterion.id)
                    
                    course.rubrics.append(rubric)
                    assignment.rubric = rubric

                assignment.submissions = self._db_service.get_submission(course_id = course.id,
                                                                        assignment_id = 
                                                                        assignment.id)
                for submission in assignment.submissions:
                    attachments = self._db_service.get_attachment(submission_id = submission.id)
                    if attachments:
                        submission.attachment = attachments[0]
                    assessments = self._db_service.get_assessment(submission_id = submission.id)
                    if assessments:
                        submission.assessments = assessments
                        
            enrolled_users = set()
            enrollments: list[Enrollment] = self._db_service.get_enrollment(course_id = course.id)
            for enrollment in enrollments: 
                users: list[User] = self._db_service.get_user(enrollment.user_id)
                for user in users:
                    if user.id not in enrolled_users:
                        user.enrollments.append(enrollment)
                        course.users.append(user)
                        enrolled_users.add(user.id)

        return courses

    def update_data(self, course_id: str, assignment_id: str = None, user_id: str = None):
        pass

    def delete_data(self, course_id: str, assignment_id: str = None, user_id: str = None):
        pass

    def get_attachment_content(self, attachment: Attachment, filters: list[str] = []) -> str:
        if attachment.file_extension == FileExtension.PDF:
            content = pdf_content_from_url(attachment.file_url)
            filtered_content = self.filter_out_content(content, filters)

            return filtered_content
        
        return ""
    
    def get_external_file_content(self, filters: list[str] = []):
        root = Tk()
        root.withdraw()
        
        file_path = filedialog.askopenfilename(
            title="Select an external file (only PDF Supported)",
            filetypes=[("PDF files", "*.pdf")]
        )

        if file_path:
            external_content = pdf_content_from_file_path(file_path)
            filtered_external_content = self.filter_out_content(external_content, filters)

            return filtered_external_content

        return ""
    
    def clear_prompt(self):
        clear_json_file(PROMPT_FILEPATH)

    def build_prompt(self, **data_content):
        template_content = read_txt_file(PROMPT_TEMPLATE_FILEPATH)
        template = Template(template_content)
        rendered_data = template.render(**data_content)
        
        self.add_message(rendered_data)

    def generate_response(self, **options):
        prompt = load_json_file(PROMPT_FILEPATH)
        response = self._llm_service.generate_response(prompt, **options)
        write_txt_file(RESPONSE_FILEPATH, response)

    def publish_submission_feedback(self, course_id: str, assignment_id: str, user_id: str):
        comment = read_txt_file(RESPONSE_FILEPATH)
        self._lms_service.put_submission_comment(course_id, assignment_id, user_id, comment)

