from fastapi import APIRouter, Body, Path

from postgres_workers.bets_worker import BetsDataWorker
from validation_classes.bets_validator import BetDataValidator, BetUpdateDataValidator

bets_router = APIRouter()
data_worker = BetsDataWorker()


@bets_router.get("/bet/get/{idn}")
def read_bet_record(idn: str) -> list:
    return data_worker.read_bet_record(idn)


@bets_router.post("/bet/add")
def create_bet_record(data: BetDataValidator = Body()) -> dict:
    return data_worker.create_bet_record(data.dict())


@bets_router.put("/bet/change/{idn}")
def update_bet_record(idn: int = Path(gt=0), data: BetUpdateDataValidator = Body()) -> dict:
    return data_worker.update_bet_record(idn, data.dict())


@bets_router.delete("/bet/delete/{idn}")
def delete_bet_record(idn: str):
    return data_worker.delete_bet_record(idn)
