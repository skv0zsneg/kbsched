from enum import Enum
from collections import namedtuple
from typing import Optional, Tuple, Union, Literal, List


class SqlPyTypes(Enum):
    T_INT = (int, 'INTEGER')
    T_NONE = (None, 'NULL')
    T_FLOAT = (float, 'REAL')
    T_STR = (str, 'TEXT')
    T_BYTES = (bytes, 'BLOB')

    def __init__(self, pi_type, sql_type):
        self.pi_type = pi_type
        self.sql_type = sql_type

    @staticmethod
    def get_sql_types() -> List[str]:
        return [v.sql_type for v in SqlPyTypes]

    @staticmethod
    def get_pi_types() -> List[None, type]:
        return [v.pi_type for v in SqlPyTypes]


class Queries:
    def __init__(self, query: Optional[str] = None):
        self.query = query

    @staticmethod
    def create_table(table_name: str,
                     fields: List[Field],
                     if_not_exist: bool = False) -> str:
        template = f"""
        CREATE TABLE {"IF NOT EXISTS" if if_not_exist else ""} {table_name} (
            {', '.join(' '.join((f.field_name, f.field_type, f.field_params)) for f in fields)}
        )
        """
        return template


class TableHandler:
    Field: namedtuple = namedtuple('Fields', ['field_name', 'field_type', 'field_params'])
    SQL_TYPES = Literal['INTEGER', 'NULL', 'REAL', 'TEXT', 'BLOB']

    def __init__(self,
                 table_name: str,
                 table_fields: List[
                     Tuple[str, Union[type, None, SQL_TYPES], str],
                     Field
                 ]):
        self.table_name = table_name
        self.table_fields = table_fields


if __name__ == "__main__":
    my_tab = TableHandler(table_name='course',
                          table_fields=[('course_id', 'INTEGER', '')])
