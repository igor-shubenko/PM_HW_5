import os

from fastapi import FastAPI

from task_maker import TaskMaker

url = os.getenv("CRUD_SERVER_LINK")


def startup_event_handler(app: FastAPI):
    async def wrapper():
        app.task_maker = TaskMaker(url)
    return wrapper

def shutdown_event_handler(app: FastAPI):
    async def wrapper():
        app.task_maker.stop()
    return wrapper()







