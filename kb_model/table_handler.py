from typing import Optional, Tuple, List


class Queries:
    @staticmethod
    def create_table(table_name: str,
                     fields: List[Tuple[str, str, Optional[str]]],
                     foreign_keys: List[Tuple[str, str, Optional[str]]] = None,
                     if_not_exist: bool = False) -> str:
        template = f"""
        CREATE TABLE {"IF NOT EXISTS" if if_not_exist else ""} {table_name} (
            {', '.join(' '.join((f[0], f[1], f[2] if f[2] is not None else "")) for f in fields)}
            {', ' + ', '.join(f"FOREIGN KEY ({k[0]}) REFERENCES {k[1]} ({k[0]}) {k[2]}" for k in foreign_keys)
            if foreign_keys is not None else ''}
        );
        """
        return template.strip()

    @staticmethod
    def insert_into(table_name: str,
                    *values: str) -> str:
        NOT_STR = ['NULL']
        values = tuple(map(lambda v: '"' + v + '"' if not v.isdigit() and v not in NOT_STR else v, values))
        template = f"""
            INSERT INTO {table_name}
            VALUES ({', '.join(v for v in values)});
        """
        return template.strip()


class TableHandler:
    def __init__(self,
                 table_name: str,
                 table_fields: List[Tuple[str, str, Optional[str]]]):
        """Table Handler. For easy manage with SQL tables.

        :param table_name: Table name.
        :param table_fields: List of values. [(field_name, field_type, additional_params)]
        """
        self.table_name = table_name
        self.table_fields = table_fields
    
    def create_table(self, 
                    foreign_keys: List[Tuple[str, str, Optional[str]]] = None, 
                    if_not_exist=False) -> str:
        return Queries.create_table(self.table_name, 
                                    self.table_fields,
                                    foreign_keys=foreign_keys,
                                    if_not_exist=if_not_exist)
    
    def insert_into(self, *values) -> str:
        if len(values) != len(self.table_fields):
            return ''
        return Queries.insert_into(self.table_name, *values)
