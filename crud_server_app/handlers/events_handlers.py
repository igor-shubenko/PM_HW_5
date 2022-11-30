from fastapi import FastAPI
from psycopg_pool import ConnectionPool

connection_string = "host=database port=5432 dbname=pm_db connect_timeout=10 user=pm_user password=12131415"

pool = ConnectionPool(connection_string, open=False)

def startup_event_handler(app: FastAPI):
    def wrapper():
        pool.open()
    return wrapper

def shutdown_event_handler(app: FastAPI):
    def wrapper():
        pool.close()
    return wrapper