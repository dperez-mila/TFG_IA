
from . import Repository
from ..database import DataManagement
from ..models import Course

class CourseRepository(Repository):

    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "course"
        self._initialize_course_table()

    def _initialize_course_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                language TEXT NOT NULL
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Course):
        insert_query = f"INSERT INTO {self._table_name} (id, name, language) VALUES (?, ?, ?)"
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.name, item.language))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> Course:
        select_query = f"SELECT name, language FROM {self._table_name} WHERE id = ?"
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Course(id=identifier, name=result[0][0], language=result[0][1])
        return None
    
    def get_all(self):
        select_query = f"SELECT id, name, language FROM {self._table_name}"
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Course(id=row[0], name=row[1], language=row[2]) for row in results]
    
    def update(self, item: Course):
        update_query = f"UPDATE {self._table_name} SET name = ?, language = ? WHERE id = ?"
        self._db_manager.execute_query(update_query, (item.name, item.language, item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
