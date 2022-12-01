from fastapi import APIRouter, Body, Path, Request

from validation_classes.events_validator import EventDataValidator, EventUpdateDataValidator

events_router = APIRouter()


@events_router.get("/event/get/{idn}")
def read_event_record(request: Request, idn: str) -> list:
    return request.app.event_data_worker.read_record(idn)


@events_router.post('/event/add')
def create_event_record(request: Request, data: EventDataValidator = Body()) -> dict:
    return request.app.event_data_worker.create_record(data.dict())


@events_router.put('/event/change/{idn}')
def update_event_record(request: Request, idn: int = Path(gt=0), data: EventUpdateDataValidator = Body()) -> dict:
    return request.app.event_data_worker.update_record(idn, data.dict())


@events_router.delete('/event/delete/{idn}')
def delete_event_record(request: Request, idn: str) -> dict:
    return request.app.event_data_worker.delete_record(idn)
