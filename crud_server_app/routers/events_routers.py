from fastapi import APIRouter, Body, Path, Request

from validation_classes.events_validator import EventDataValidator, EventUpdateDataValidator

events_router = APIRouter()


@events_router.get("/event/get/{idn}")
async def read_event_record(request: Request, idn: str) -> list:
    return await request.app.event_data_worker.read_record(idn)


@events_router.post('/event/add')
async def create_event_record(request: Request, data: EventDataValidator = Body()) -> dict:
    return await request.app.event_data_worker.create_record(data.dict())


@events_router.put('/event/change/{idn}')
async def update_event_record(request: Request, idn: int = Path(gt=0), data: EventUpdateDataValidator = Body()) -> dict:
    return await request.app.event_data_worker.update_record(idn, data.dict())


@events_router.delete('/event/delete/{idn}')
async def delete_event_record(request: Request, idn: str) -> dict:
    return await request.app.event_data_worker.delete_record(idn)
