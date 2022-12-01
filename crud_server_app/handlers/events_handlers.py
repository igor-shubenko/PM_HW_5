import os

from fastapi import FastAPI
from psycopg_pool import ConnectionPool

connection_string = os.environ.get("DATABASE_LINK")

pool = ConnectionPool(connection_string, open=False)


def startup_event_handler(app: FastAPI):
    def wrapper():
        pool.open()
    return wrapper


def shutdown_event_handler(app: FastAPI):
    def wrapper():
        pool.close()
    return wrapper