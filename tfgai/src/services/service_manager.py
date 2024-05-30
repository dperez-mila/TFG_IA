
from jinja2 import Template
from .llm_services import LLMService
from .lms_services import LMSService
from .database_services import DataManagementService
from ..core import PROMPT_TEMPLATE_FILEPATH, PROMPT_FILEPATH, RESPONSE_FILEPATH
from ..models import Rubric, Criterion, Rating, Submission, Assignment, Attachment
from ..utils import load_json_file, dump_json_file, clear_json_file
from ..utils import extract_text_from_pdf_url
from ..utils import read_txt_file, write_txt_file


class ServiceManager():

    def __init__(self, llm_service: LLMService, lms_service: LMSService, 
                 db_service: DataManagementService):
        self._llm_service = llm_service
        self._lms_service = lms_service
        self._db_service = db_service

    def _build_data(self, **data_content):
        template_content = read_txt_file(PROMPT_TEMPLATE_FILEPATH)
        template = Template(template_content)
        rendered_data = template.render(**data_content)
        print(rendered_data)
        return rendered_data

    def add_message(self, content: str, role: str = "user"):
        messages = load_json_file(PROMPT_FILEPATH)
        messages.append({"role": role, "content": content})
        dump_json_file(PROMPT_FILEPATH, messages)

    def get_course_data(self, course_id: str):
        course = self._db_service.get_course(course_id)
        if not course: 
            return None
        return course

    def get_assignment_data(self, assignment_id: str) -> Assignment:
        assignment = self._db_service.get_assignment(assignment_id)
        if not assignment:
            return None
        return assignment
    
    def get_rubric_data(self, rubric_id: str):
        rubric = self._db_service.get_rubric(rubric_id)
        if not rubric:
            return None
        return rubric
    
    def get_submission_data(self, assignment_id: str, user_id: str) -> Submission:
        submission = self._db_service.get_submission(assignment_id, user_id)
        if not submission:
            return None
        return submission
    
    def get_assessed_rubric_data(self, rubric: Rubric, submission: Submission) -> Rubric:
        assessed_criteria = []
        for assessment in submission.assessments:
            for criterion in rubric.criteria:
                if assessment.criterion_id == criterion.id:
                    for rating in criterion.ratings:
                        if assessment.rating_id == rating.id:
                            assessed_rating = Rating(rating.id, rating.criterion_id, rating.description, 
                                                     rating.long_description, rating.max_score)
                            assessed_rating.comment = assessment.comment
                            assessed_criterion = Criterion(criterion.id, criterion.rubric_id, 
                                                           criterion.description, 
                                                           criterion.long_description, 
                                                           criterion.max_score, [assessed_rating])
                            assessed_criteria.append(assessed_criterion)
        assessed_rubric = Rubric(rubric.id, rubric.course_id, rubric.title, rubric.max_score, 
                                 assessed_criteria)
        return assessed_rubric
        

    def get_attachment_content(self, attachment: Attachment) -> str:
        if attachment.type == "pdf":
            return extract_text_from_pdf_url(attachment.url)
        return None
    
    def refresh_course_data(self, course_id: str):
        course = self._lms_service.get_course(course_id)
        if not self._db_service.get_course(course_id):
            self._db_service.add_course(course)
        else:
            self._db_service.update_course(course)

    def refresh_assignment_data(self, course_id: str, assignment_id: str):
        assignment = self._lms_service.get_assignment(course_id, assignment_id)
        if not self._db_service.get_assignment(assignment_id):
            self._db_service.add_assignment(assignment)
        else:
            self._db_service.update_assignment(assignment)
    
    def refresh_rubric_data(self, course_id: str, assignment_id: str):
        rubric_id = self._get_assignment_data(assignment_id).rubric_id
        rubric = self._lms_service.get_rubric(course_id, rubric_id)
        if not self._db_service.get_rubric(rubric_id):
            self._db_service.add_rubric(rubric)
        else:
            self._db_service.update_rubric(rubric)

    def refresh_submission_data(self, course_id: str, assignment_id: str, user_id: str):
        submission = self._lms_service.get_submission(course_id, assignment_id, user_id)
        if not self._db_service.get_submission(assignment_id, user_id):
            self._db_service.add_submission(submission)
        else:
            self._db_service.update_submission(submission)
    
    def clear_prompt(self): 
        clear_json_file(PROMPT_FILEPATH)

    def build_prompt(self, **data_content):
        data = self._build_data(**data_content)
        self.add_message(data)

    def generate_response(self): 
        prompt = load_json_file(PROMPT_FILEPATH)
        response = self._llm_service.generate_response(prompt)
        print(response)
        write_txt_file(RESPONSE_FILEPATH, response)

