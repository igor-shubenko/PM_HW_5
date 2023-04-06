import concurrent.futures

import httpx
import asyncio

from math_operations.median_calculator import MedianCalculator
from math_operations.age_range_calculator import AgeRangeCalculator
from math_operations.unique_names_hystogram import UniqueNamesCalculator


class TaskMaker:
    def __init__(self, url):
        self._url = url
        self._client = httpx.AsyncClient()
        self._executor = concurrent.futures.ThreadPoolExecutor()
        self._median = MedianCalculator()
        self._age_range = AgeRangeCalculator()
        self._unique_names = UniqueNamesCalculator()

    async def _execute(self, inst, *args):
        try:
            data = await self._client.get(self._url, timeout=100)
        except Exception:
            return {"Error": "Something wrong"}
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(self._executor, inst, data.json(), *args)
        return result

    async def median(self):
        return await self._execute(self._median)

    async def unique_names_histogram(self):
        return await self._execute(self._unique_names)

    async def age_range(self, frm: int, to: int):
        return await self._execute(self._age_range, frm, to)

    def stop(self):
        self._executor.shutdown()
