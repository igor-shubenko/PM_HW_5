import os

from fastapi import FastAPI
import asyncio
import uvicorn
import httpx
import concurrent.futures
from math_operations import MedianCalculator, UniqueNamesCalculator, AgeRangeCalculator

math_operations_server = FastAPI(title="Math Operations Server",
                                 description="Server provides math operations with users data",
                                 version="2.0")

url = os.getenv("CRUD_SERVER_LINK")
client = httpx.AsyncClient()
executor = concurrent.futures.ThreadPoolExecutor()

@math_operations_server.get("/test")
async def test():
    response = await client.get(url, timeout=100)
    return response.json()


@math_operations_server.get("/median")
async def median():
    response = await client.get(url, timeout=100)
    loop = asyncio.get_running_loop()
    inst = MedianCalculator(response.json())
    result = await loop.run_in_executor(executor, inst)
    return result

@math_operations_server.get("/unique_names_histogram")
async def unique_names_histogram():
    response = await client.get(url, timeout=100)
    loop = asyncio.get_running_loop()
    inst = UniqueNamesCalculator(response.json())
    result = await loop.run_in_executor(executor, inst)
    return result

@math_operations_server.get("/age_range")
async def age_range(frm: int, to: int):
    response = await client.get(url, timeout=100)
    loop = asyncio.get_running_loop()
    inst = AgeRangeCalculator(response.json())
    result = await loop.run_in_executor(executor, inst, frm, to)
    return result


if __name__ == '__main__':
    uvicorn.run("math_operations_server:math_operations_server", host='0.0.0.0', port=8766, reload=True)
