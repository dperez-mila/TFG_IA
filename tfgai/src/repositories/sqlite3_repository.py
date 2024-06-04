
import logging

from dataclasses import fields, MISSING
from typing import Type, TypeVar, get_origin, get_args, get_type_hints
from types import UnionType
from enum import Enum
import importlib

from .repository import Repository
from ..models import Model
from ..database import SQLiteDataManagement
from ..enums import Language, FileExtension, EnrollmentType


T = TypeVar('T', bound=Model)

class SQLite3Repository(Repository[T]):

    def __init__(self, db_path: str, model_cls: Type[T]):
        self._db_manager = SQLiteDataManagement(db_path)
        self._model_cls = model_cls
        self._table = model_cls.__name__.lower() + 's'
        self._create_table()

    def _class_from_srt(self, module_path: str, class_name: str) -> type:
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    def _obj_to_tuple(self, obj: T) -> zip:
        keys = []
        values = []

        for field in fields(obj):
            key = field.name
            value = getattr(obj, key)
            _type = field.type

            origin = get_origin(_type)
            args = get_args(_type)

            if origin is UnionType and type(None) in args:
                _type = next(t for t in args if t is not type(None))

            if origin in (list,) or isinstance(_type, type) and issubclass(_type, Model):
                continue

            if isinstance(value, Enum):
                value = value.value
            elif isinstance(value, type) and issubclass(value, Model):
                value = value.__name__

            keys.append(key)
            values.append(value)

        return zip(keys, values)
    
    def _tuple_to_obj(self, keys: tuple, data: tuple) -> T:
        field_names = [field.name for field in fields(self._model_cls)]
        field_types = [field.type for field in fields(self._model_cls)]
        values = []

        for field_name in field_names:
            field_type = field_types[field_names.index(field_name)]
            field_type_origin = get_origin(field_type)
            field_type_args = get_args(field_type)

            if field_name in keys:
                value = data[keys.index(field_name)]

                if issubclass(field_type, Enum):
                    for member in field_type:
                        if member.value == value:
                            value = member
                elif isinstance(field_type_origin, type) and issubclass(field_type_args[0], Model):
                    value = self._class_from_srt("src.models", value)

                values.append(value)

        return self._model_cls(*values)

    def _execute_query(self, query: str, params: tuple = ()):
        with self._db_manager as db:
            try:
                db.execute_query(query, params)
            except Exception as e:
                logging.error(f'''
                    Error executing sqlite3 query: {e}
                        - Query: {query}
                        - Values: {params}
                ''')

    def _fetch_results(self, query: str, params: tuple = ()) -> list[tuple]:
        with self._db_manager as db:
            try:
                db.execute_query(query, params)
                results = db.fetch_results()
                description = db.get_description()
            except Exception as e:
                logging.error(f'''
                    Error fetching sqlite3 results: {e}
                        - Query: {query}
                        - Values: {params}
                ''')

        if results and description:
            keys = tuple([key[0] for key in description])
            return [(keys, row) for row in results]
        
        return []
    
    def _create_table(self):
        fields_list = []
        foreign_keys = []
        type_mapping = {
            int: "INTEGER",
            float: "REAL",
            str: "TEXT",
            bool: "INTEGER",
            Language: "TEXT",
            FileExtension: "TEXT",
            EnrollmentType: "TEXT"
        }
    
        for name, _type in get_type_hints(self._model_cls).items():
            is_primary_key = False

            origin = get_origin(_type)
            args = get_args(_type)

            if origin is UnionType and type(None) in args:
                _type = next(t for t in args if t is not type(None))

            if origin in (list,) or isinstance(_type, type) and issubclass(_type, Model):
                continue

            if name == "id":
                is_primary_key = True
            elif "_id" in name:
                foreign_keys.append(f"FOREIGN KEY({name}) REFERENCES {name.split('_id')[0]}s(id)")

            if _type in type_mapping:
                field_type = (
                    f"{type_mapping[_type]} PRIMARY KEY" 
                    if is_primary_key else 
                    type_mapping[_type]
                )
            elif isinstance(origin, type) and issubclass(args[0], Model):
                field_type = type_mapping[str]
            else:
                raise TypeError(f"Unsupported field type {_type} for field {name}")
            
            field = next(f for f in fields(self._model_cls) if f.name == name)
            if not is_primary_key and field.default == MISSING and field.default_factory == MISSING:
                field_type += " NOT NULL"

            fields_list.append(f"{name} {field_type}")

        field_definitions = ", ".join(fields_list + foreign_keys)
        query = f"CREATE TABLE IF NOT EXISTS {self._table} ({field_definitions})"

        self._execute_query(query)

    def add(self, obj: T):
        keys_tuple, values_tuple = zip(*self._obj_to_tuple(obj))

        keys_str = ", ".join(keys_tuple)
        placeholders = ", ".join(['?' for _ in values_tuple])
        query = f"INSERT INTO {self._table} ({keys_str}) VALUES ({placeholders})"

        self._execute_query(query, values_tuple)

    def get(self, obj_id: str = None, **conditions) -> list[T]:
        values = []

        if not obj_id and not conditions: 
            query = f"SELECT * FROM {self._table}"
        else:
            keys = []

            if obj_id:
                keys.append("id")
                values.append(obj_id)
            if conditions:
                keys.extend(conditions.keys())
                values.extend(conditions.values())

            where_clause = " AND ".join([f"{key} = ?" for key in keys])
            query = f"SELECT * FROM {self._table} WHERE {where_clause}"

        results = self._fetch_results(query, tuple(values))
        
        return [self._tuple_to_obj(keys, data) for keys, data in results]
        
    def update(self, obj_id: str, obj: T):
        keys_tuple, values_tuple = zip(*self._obj_to_tuple(obj))

        if "id" in keys_tuple:
            index = keys_tuple.index("id")
            keys_tuple = keys_tuple[:index] + keys_tuple[index + 1:]
            values_tuple = values_tuple[:index] + values_tuple[index + 1:]

        values_tuple += (obj_id,)
        set_clause = ", ".join([f"{key} = ?" for key in keys_tuple])
        query = f"UPDATE {self._table} SET {set_clause} WHERE id = ?"

        self._execute_query(query, values_tuple)

    def delete(self, obj_id: str):
        query = f"DELETE FROM {self._table} WHERE id = ?"

        self._execute_query(query, (obj_id,))

