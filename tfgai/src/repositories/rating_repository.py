
from . import Repository
from ..database import DataManagement
from ..models import Rating


class RatingRepository(Repository):
    
    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "rating"
        self._initialize_course_table()

    def _initialize_course_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                criterion_id TEXT NOT NULL,
                description TEXT NOT NULL,
                long_description TEXT NOT NULL,
                max_score REAL NOT NULL
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Rating):
        insert_query = f'''
            INSERT INTO {self._table_name} (id, criterion_id, description, long_description, max_score) 
            VALUES (?, ?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.criterion_id, item.description, 
                                                          item.long_description, item.max_score))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> Rating:
        select_query = f'''
            SELECT criterion_id, description, long_description, max_score FROM {self._table_name}
            WHERE id = ?
        '''
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Rating(id=identifier, criterion_id=result[0][0], description=result[0][1],
                             long_description=result[0][2], max_score=result[0][3])
        return None
    
    def get_by_criterion(self, criterion_id: str) -> list[Rating]:
        select_query = f'''
            SELECT id, description, long_description, max_score FROM {self._table_name}
            WHERE criterion_id = ?
        '''
        self._db_manager.execute_query(select_query, (criterion_id,))
        results = self._db_manager.fetch_results()
        return [Rating(id=row[0], criterion_id=criterion_id, description=row[1], long_description=row[2],
                          max_score=row[3]) for row in results]
    
    def get_all(self):
        select_query = f'''
            SELECT id, criterion_id, description, long_description, max_score FROM {self._table_name}
        '''
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Rating(id=row[0], criterion_id=row[1], description=row[2], long_description=row[3],
                          max_score=row[4]) for row in results]
    
    def update(self, item: Rating):
        update_query = f'''
            UPDATE {self._table_name} SET description = ?, long_description = ?, max_score = ? 
            WHERE id = ?
        '''
        self._db_manager.execute_query(update_query, (item.description, item.long_description, 
                                                      item.max_score, item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
