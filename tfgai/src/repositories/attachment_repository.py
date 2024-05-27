
from . import Repository
from ..database import DataManagement
from ..models import Attachment

class AttachmentRepository(Repository):
    
    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "attachment"
        self._initialize_attachment_table()

    def _initialize_attachment_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                submission_id TEXT NOT NULL,
                file_name TEXT NOT NULL,
                url TEXT NOT NULL,
                type TEXT NOT NULL,
                size REAL NOT NULL
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: Attachment):
        insert_query = f'''
            INSERT INTO {self._table_name} (id, submission_id, file_name, url, type, size) 
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.submission_id, item.file_name, 
                                                          item.url, item.type, item.size))
        except Exception as e:
            print(f"(Attachment) An error was raised: {e}!")
    
    def get(self, identifier: str) -> Attachment:
        select_query = f'''
            SELECT submission_id, file_name, url, type, size FROM {self._table_name} WHERE id = ?
        '''
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"(Attachment) An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return Attachment(id=identifier, submission_id=result[0][0], file_name=result[0][1],
                              url=result[0][2], type=result[0][3], size=result[0][4])
        return None
    
    def get_by_submission(self, submission_id: str) -> Attachment:
        select_query = f'''
            SELECT id, file_name, url, type, size FROM {self._table_name}
            WHERE submission_id = ?
        '''
        self._db_manager.execute_query(select_query, (submission_id,))
        results = self._db_manager.fetch_results()
        return [Attachment(id=row[0], submission_id=submission_id, file_name=row[1], url=row[2], 
                           type=row[3], size=row[4]) for row in results]

    def get_all(self):
        select_query = f'''
            SELECT id, submission_id, file_name, url, type, size FROM {self._table_name}
        '''
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [Attachment(id=row[0], submission_id=row[1], file_name=row[2], url=row[3], type=row[4], 
                           size=row[5]) for row in results]
    
    def update(self, item: Attachment):
        update_query = f'''
            UPDATE {self._table_name} SET file_name = ?, url = ?, type = ?, size = ? WHERE id = ?
        '''
        self._db_manager.execute_query(update_query, (item.file_name, item.url, item.type, item.size, 
                                                      item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))
    
