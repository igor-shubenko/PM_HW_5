from postgres_workers.main_worker import MainDatabaseWorker
from psycopg_pool import ConnectionPool
from fastapi import HTTPException

class QueryMaker(MainDatabaseWorker):
    def __init__(self, pool: ConnectionPool = None,
                 table_name: str = None,
                 cols_names: tuple = None):
        self._pool = pool
        self._table_name = table_name
        self._cols_names = ', '.join(cols_names)
        self._cols_amount = len(cols_names)

    async def create_record(self, data: dict) -> dict:
        query = f"INSERT INTO {self._table_name}({self._cols_names}) VALUES" \
                f"({', '.join(['%s']*self._cols_amount)});"
        values = tuple(data.values())
        return await self._create_record(query, values)

    async def read_record(self, idn: str) -> list | dict:
        if idn == 'all':
            query = f'SELECT * FROM {self._table_name} ORDER BY id;'
        elif idn.isdigit():
            query = f'SELECT * FROM {self._table_name} WHERE id={idn};'
        else:
            raise HTTPException(status_code=400, detail={"Error": "Wrong identificator"})

        return await self._read_record(query)

    async def update_record(self, idn: int, data: dict) -> dict:
        data = {k: v for k, v in data.items() if v is not None}
        query_start = f"UPDATE {self._table_name} SET "
        temp_strings = []

        for k, v in data.items():
            if type(v) is str:
                temp_string = f"{k}='{v}'"
            else:
                temp_string = f"{k}={v}"
            temp_strings.append(temp_string)
        query = query_start + ', '.join(temp_strings) + f' WHERE id={idn};'

        return await self._update_record(query)

    async def delete_record(self, idn: str):
        if idn == 'all':
            query = f'TRUNCATE {self._table_name} CASCADE;'
        elif idn.isdigit():
            query = f'DELETE FROM {self._table_name} WHERE id={idn};'
        else:
            raise HTTPException(status_code=400, detail={"Error": "Wrong identificator"})

        return await self._delete_record(query)


