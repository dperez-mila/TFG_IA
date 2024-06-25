
from . import LMSClient


class CanvasClient(LMSClient):

    def get_courses(self, course_id: str = None) -> list[dict]:
        if not course_id:
            return self._get("courses")
        
        return [self._get(f"courses/{course_id}")]
    
    def get_assignments(self, course_id: str, assignment_id: str = None) -> list[dict]:
        if not assignment_id:
            return self._get(f"courses/{course_id}/assignments")
        
        return [self._get(f"courses/{course_id}/assignments/{assignment_id}")]
    
    def get_rubrics(self, course_id: str, rubric_id: str = None) -> list[dict]:
        params = {"include[]": ["associations", "assessments"]}

        if not rubric_id:
            return self._get(f"courses/{course_id}/rubrics", params)
        
        return [self._get(f"courses/{course_id}/rubrics/{rubric_id}", params)]
    
    def get_submissions(self, course_id: str, assignment_id: str, user_id: str = None) -> list[dict]:
        params = {"include[]": "full_rubric_assessment"}

        if not user_id:
            return self._get(f"courses/{course_id}/assignments/{assignment_id}/submissions", params)
        
        return [self._get(f"courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}",
                         params)] 
    
    def get_attachments(self, attachment_id: str = None):
        params = {"include[]": "user"}

        if not attachment_id:
            return self._get("files", params)
        
        return [self._get(f"files/{attachment_id}", params)]

    def get_users(self, course_id: str, user_id: str = None) -> list[dict]:
        params = {"include[]": "enrollments"}
        if not user_id:
            return self._get(f"courses/{course_id}/users", params)
        
        return [self._get(f"courses/{course_id}/users/{user_id}", params)]

    def put_submission_comment(self, course_id: str, assignment_id: str, user_id: str, data: dict):
        self._put(f"courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}", data)

    def put_rubric_assessment_comments(self, course_id: str, rubric_association_id: str,
                                      rubric_assessment_id: str, rubric_assessment_data: dict):
        endpoint = (
            f"courses/{course_id}"
            f"/rubric_associations/{rubric_association_id}"
            f"/rubric_assessments/{rubric_assessment_id}"
        )
        data = {
            **rubric_assessment_data
        }
        
        self._put(endpoint, data)

