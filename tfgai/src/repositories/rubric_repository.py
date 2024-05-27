
from . import Repository
from ..database import DataManagement
from ..models import Rubric

class RubricRepository(Repository):
    
    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "rubric"
        self._initialize_course_table()

    def _initialize_course_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                course_id TEXT NOT NULL,
                title TEXT NOT NULL,
                max_score TEXT NOT NULL 
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Rubric):
        insert_query = f'''
            INSERT INTO {self._table_name} (id, course_id, title, max_score) VALUES (?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.course_id, item.title, 
                                                          item.max_score))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> Rubric:
        select_query = f"SELECT course_id, title, max_score FROM {self._table_name} WHERE id = ?"
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Rubric(id=identifier, course_id=result[0][0], title=result[0][1], 
                          max_score=result[0][2])
        return None
    
    def get_all(self):
        select_query = f"SELECT id, course_id, title, max_score FROM {self._table_name}"
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Rubric(id=row[0], course_id=row[1], title=row[2], max_score=row[3]) for row in results]
    
    def update(self, item: Rubric):
        update_query = f"UPDATE {self._table_name} SET title = ?, max_score = ? WHERE id = ?"
        self._db_manager.execute_query(update_query, (item.title, item.max_score, item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
