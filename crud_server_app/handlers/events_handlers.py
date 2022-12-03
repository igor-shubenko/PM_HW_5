import os

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from postgres_workers.users_worker import UserDataWorker
from postgres_workers.events_worker import EventsDataWorker
from postgres_workers.bets_worker import BetsDataWorker

connection_string = os.environ.get("DATABASE_LINK")
pool = AsyncConnectionPool(connection_string, open=False)


def startup_event_handler(app: FastAPI):
    async def wrapper():
        app.user_data_worker = UserDataWorker(pool=pool)
        app.event_data_worker = EventsDataWorker(pool=pool)
        app.bet_data_worker = BetsDataWorker(pool=pool)
        await pool.open(wait=True)
    return wrapper


def shutdown_event_handler(app: FastAPI):
    async def wrapper():
        await pool.close()
    return wrapper
