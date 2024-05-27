
from . import Repository
from ..database import DataManagement
from ..models import Submission

class SubmissionRepository(Repository):
    
    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "submission"
        self._initialize_course_table()

    def _initialize_course_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                assignment_id TEXT NOT NULL,
                student_id TEXT NOT NULL,
                grader_id TEXT NOT NULL,
                score REAL NOT NULL,
                late INTEGER NOT NULL
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Submission):
        insert_query = f'''
            INSERT INTO {self._table_name} (id, assignment_id, student_id, grader_id, score, late) 
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.assignment_id, item.student_id, 
                                                          item.grader_id, item.score, 
                                                          1 if item.late == True else 0))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> Submission:
        select_query = f'''
            SELECT assignment_id, student_id, grader_id, score, late FROM {self._table_name}
            WHERE id = ?
        '''
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Submission(id=identifier, assignment_id=result[0][0], student_id=result[0][1],
                             grader_id=result[0][2], score=result[0][3], 
                             late=True if result[0][4] == 1 else False)
        return None
    
    def get_by_assignment_user(self, assignment_id: str, user_id: str) -> list[Submission]:
        select_query = f'''
            SELECT id, grader_id, score, late FROM {self._table_name} 
            WHERE assignment_id = ? AND student_id = ?
        '''
        self._db_manager.execute_query(select_query, (assignment_id, user_id))
        results = self._db_manager.fetch_results()
        return [Submission(id=row[0], assignment_id=assignment_id, student_id=user_id, grader_id=row[1],
                          score=row[2], late= True if row[3] == 1 else False) for row in results]
    
    def get_all(self):
        select_query = f'''
            SELECT id, assignment_id, student_id, grader_id, score, late FROM {self._table_name}
        '''
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Submission(id=row[0], assignment_id=row[1], student_id=row[2], grader_id=row[3],
                          score=row[4], late= True if row[5] == 1 else False) for row in results]
    
    def update(self, item: Submission):
        update_query = f"UPDATE {self._table_name} SET score = ?, late = ? WHERE id = ?"
        self._db_manager.execute_query(update_query, (item.score, 1 if item.late == True else 0, 
                                                      item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
