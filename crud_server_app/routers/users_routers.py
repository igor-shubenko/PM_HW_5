from fastapi import APIRouter, Body, Path

from postgres_workers.users_worker import UserDataWorker
from validation_classes.users_validator import UserDataValidator, UserUpdateDataValidator

users_router = APIRouter()
data_worker = UserDataWorker()

@users_router.get("/get/{idn}")
def read_user_record(idn: str) -> list:
    return data_worker.read_user_record(idn)


@users_router.post('/add')
def create_user_record(data: UserDataValidator = Body()) -> dict:
    return data_worker.create_user_record(data.dict())


@users_router.put('/change/{idn}')
def update_user_record(idn: int = Path(gt=0), data: UserUpdateDataValidator = Body()) -> dict:
    return data_worker.update_user_record(idn, data.dict())


@users_router.delete('/delete/{idn}')
def delete_user_record(idn: str) -> dict:
    return data_worker.delete_user_record(idn)
