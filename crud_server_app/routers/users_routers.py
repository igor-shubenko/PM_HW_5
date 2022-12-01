from fastapi import APIRouter, Body, Path, Request

from validation_classes.users_validator import UserDataValidator, UserUpdateDataValidator

users_router = APIRouter()


@users_router.get("/get/{idn}")
def read_user_record(request: Request, idn: str) -> list:
    return request.app.user_data_worker.read_record(idn)


@users_router.post('/add')
def create_user_record(request: Request, data: UserDataValidator = Body()) -> dict:
    return request.app.user_data_worker.create_record(data.dict())


@users_router.put('/change/{idn}')
def update_user_record(request: Request, idn: int = Path(gt=0), data: UserUpdateDataValidator = Body()) -> dict:
    return request.app.user_data_worker.update_record(idn, data.dict())


@users_router.delete('/delete/{idn}')
def delete_user_record(request: Request, idn: str) -> dict:
    return request.app.user_data_worker.delete_record(idn)
