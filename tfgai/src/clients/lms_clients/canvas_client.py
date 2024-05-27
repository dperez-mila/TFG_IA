
from . import LMSClient


class CanvasClient(LMSClient):
    
    def __init__(self, base_url, token):
        super().__init__(base_url, token)
    
    def get_courses(self):
        return self._get("courses")

    def get_course(self, course_id: str):
        return self._get(f"courses/{course_id}")
    
    def get_user(self, course_id: str, user_id: str):
        return self._get(f"courses/{course_id}/users/{user_id}")
    
    def get_rubrics(self, course_id: str):
        return self._get(f"courses/{course_id}/rubrics")
    
    def get_rubric(self, course_id: str, rubric_id: str):
        return self._get(f"courses/{course_id}/rubrics/{rubric_id}")
    
    def get_assignments(self, course_id: str):
        return self._get(f"courses/{course_id}/assignments")

    def get_assignment(self, course_id: str, assignment_id: str):
        return self._get(f"courses/{course_id}/assignments/{assignment_id}")
    
    def get_submissions(self, course_id: str, assignment_id: str):
        return self._get(f"courses/{course_id}/assignments/{assignment_id}/submissions")
    
    def get_submission(self, course_id: str, assignment_id: str, user_id: str):
        return self._get(f"courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}?include[]=full_rubric_assessment")
    
    def put_submission_comment(self, course_id: str, assignment_id: str, user_id: str, comment: str):
        pass

