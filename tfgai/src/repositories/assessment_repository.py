
from . import Repository
from ..database import DataManagement
from ..models import Assessment


class AssessmentRepository(Repository):

    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "assessment"
        self._initialize_assessment_table()

    def _initialize_assessment_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                submission_id TEXT NOT NULL,
                rubric_id TEXT NOT NULL,
                criterion_id TEXT NOT NULL,
                rating_id TEXT NOT NULL,
                score REAL NOT NULL,
                comment REAL
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Assessment):
        insert_query = f'''
            INSERT INTO {self._table_name} 
            (id, submission_id, rubric_id, criterion_id, rating_id, score, comment) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.submission_id, item.rubric_id, 
                                                          item.criterion_id, item.rating_id, item.score, 
                                                          item.comment))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> Assessment:
        select_query = f'''
            SELECT submission_id, rubric_id, criterion_id, rating_id, score, comment 
            FROM {self._table_name}
            WHERE id = ?
        '''
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Assessment(id=identifier, submission_id=result[0][0], rubric_id=result[0][1],
                              criterion_id=result[0][2], rating_id=result[0][3], score=result[0][4], 
                              comment=result[0][5])
        return None
    
    def get_by_submission(self, submission_id: str) -> list[Assessment]:
        select_query = f'''
            SELECT id, rubric_id, criterion_id, rating_id, score, comment FROM {self._table_name}
            WHERE submission_id = ?
        '''
        self._db_manager.execute_query(select_query, (submission_id,))
        results = self._db_manager.fetch_results()
        return [Assessment(id=row[0], submission_id=submission_id, rubric_id=row[1], 
                           criterion_id=row[2], rating_id=row[3], score=row[4], comment=row[5]) 
                           for row in results]
    
    def get_all(self) -> list[Assessment]:
        select_query = f'''
            SELECT id, submission_id, rubric_id, criterion_id, rating_id, score, comment 
            FROM {self._table_name}
        '''
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Assessment(id=row[0], submission_id=row[1], rubric_id=row[2], criterion_id=row[3], 
                           rating_id=row[4], score=row[5], comment=row[6]) for row in results]
    
    def update(self, item: Assessment):
        update_query = f"UPDATE {self._table_name} SET score = ?, comment = ? WHERE id = ?"
        self._db_manager.execute_query(update_query, (item.score, item.comment, item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
