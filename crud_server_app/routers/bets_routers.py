from fastapi import APIRouter, Body, Path, Request

from validation_classes.bets_validator import BetDataValidator, BetUpdateDataValidator

bets_router = APIRouter()


@bets_router.get("/bet/get/{idn}")
def read_bet_record(request: Request, idn: str, ) -> list:
    return request.app.bet_data_worker.read_record(idn)


@bets_router.post("/bet/add")
def create_bet_record(request: Request, data: BetDataValidator = Body()) -> dict:
    return request.app.bet_data_worker.create_record(data.dict())


@bets_router.put("/bet/change/{idn}")
def update_bet_record(request: Request, idn: int = Path(gt=0), data: BetUpdateDataValidator = Body()) -> dict:
    return request.app.bet_data_worker.update_record(idn, data.dict())


@bets_router.delete("/bet/delete/{idn}")
def delete_bet_record(request: Request, idn: str):
    return request.app.bet_data_worker.delete_record(idn)
