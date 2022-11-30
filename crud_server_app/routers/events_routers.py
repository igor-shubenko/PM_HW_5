from fastapi import APIRouter, Body, Path

from validation_classes.events_validator import EventDataValidator, EventUpdateDataValidator
from postgres_workers.events_worker import EventsDataWorker

events_router = APIRouter()
data_worker = EventsDataWorker()


@events_router.get("/event/get/{idn}")
def read_event_record(idn: str) -> list:
    return data_worker.read_event_record(idn)


@events_router.post('/event/add')
def create_event_record(data: EventDataValidator = Body()) -> dict:
    return data_worker.create_event_record(data.dict())


@events_router.put('/event/change/{idn}')
def update_event_record(idn: int = Path(gt=0), data: EventUpdateDataValidator = Body()) -> dict:
    return data_worker.update_event_record(idn, data.dict())


@events_router.delete('/event/delete/{idn}')
def delete_event_record(idn: str) -> dict:
    return data_worker.delete_event_record(idn)