from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from fastapi import HTTPException

class MainDatabaseWorker:
    def __init__(self, pool: ConnectionPool = None):
        self._pool = pool

    async def _execute_query(self, query: str, values: tuple = None):
        """Executes queries to database, returns Cursor object"""
        async with self._pool.connection() as conn:
            conn.row_factory = dict_row
            return await conn.execute(query, values)

    async def _create_record(self, query: str, values: tuple) -> dict:
        try:
            await self._execute_query(query, values)
        except Exception:
            raise HTTPException(status_code=500, detail="Record not created")
        return {"Success": "Record created"}

    async def _read_record(self, query: str) -> list | dict:
        try:
            result = await self._execute_query(query)
        except Exception:
            raise HTTPException(status_code=500, detail="Some Error")
        else:
            return await result.fetchall()

    async def _update_record(self, query: str) -> dict:
        try:
            await self._execute_query(query)
        except Exception:
            raise HTTPException(status_code=500, detail="Update failed")
        else:
            return {"Success": "Record updated"}

    async def _delete_record(self, query: str) -> dict:
        try:
            await self._execute_query(query)
        except Exception:
            raise HTTPException(status_code=500, detail="Error not deleted")
        return {"Success": "Record deleted"}
