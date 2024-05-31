
from . import Repository
from ..database import DataManagement
from ..models import User

class UserRepository(Repository):
    
    def __init__(self, db_manager: DataManagement):
        super().__init__(db_manager)
        self._table_name = "user"
        self._initialize_user_table()

    def _initialize_user_table(self):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                email TEXT
            )
        '''
        self._db_manager.execute_query(create_table_query)

    def add(self, item: User):
        insert_query = f'''
            INSERT INTO {self._table_name} (id, full_name, first_name, last_name, username, email) 
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        try:
            self._db_manager.execute_query(insert_query, (item.id, item.full_name, item.first_name, 
                                                          item.last_name, item.username, item.email))
        except Exception as e:
            print(f"An error was raised: {e}!")
    
    def get(self, identifier: str) -> User:
        select_query = f'''
            SELECT full_name, first_name, last_name, username, email FROM {self._table_name} WHERE id = ?
        '''
        try:
            self._db_manager.execute_query(select_query, (identifier,))
        except Exception as e:
            print(f"An error was raised: {e}!")
        result = self._db_manager.fetch_results()
        if result:
            return User(id=identifier, full_name=result[0][0], first_name=result[0][1],
                              last_name=result[0][2])
        return None
    
    def get_all(self):
        select_query = f'''
            SELECT id, full_name, first_name, last_name, username, email FROM {self._table_name}
        '''
        self._db_manager.execute_query(select_query)
        results = self._db_manager.fetch_results()
        return [User(id=row[0], full_name=row[1], first_name=row[2], last_name=row[3], username=row[4],
                     email=row[5]) 
                for row in results]
    
    def update(self, item: User):
        update_query = f'''
            UPDATE {self._table_name} 
            SET full_name = ?, first_name = ?, last_name = ?, username = ?, email = ? 
            WHERE id = ?
        '''
        self._db_manager.execute_query(update_query, (item.full_name, item.first_name, item.last_name, 
                                                      item.username, item.email, item.id))
    
    def delete(self, identifier: str):
        delete_query = f"DELETE FROM {self._table_name} WHERE id = ?"
        self._db_manager.execute_query(delete_query, (identifier,))

