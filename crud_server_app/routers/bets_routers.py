from fastapi import APIRouter, Body, Path, Request

from validation_classes.bets_validator import BetDataValidator, BetUpdateDataValidator

bets_router = APIRouter()


@bets_router.get("/bet/get/{idn}")
async def read_bet_record(request: Request, idn: str, ) -> list:
    return await request.app.bet_data_worker.read_record(idn)


@bets_router.post("/bet/add")
async def create_bet_record(request: Request, data: BetDataValidator = Body()) -> dict:
    return await request.app.bet_data_worker.create_record(data.dict())


@bets_router.put("/bet/change/{idn}")
async def update_bet_record(request: Request, idn: int = Path(gt=0), data: BetUpdateDataValidator = Body()) -> dict:
    return await request.app.bet_data_worker.update_record(idn, data.dict())


@bets_router.delete("/bet/delete/{idn}")
async def delete_bet_record(request: Request, idn: str):
    return await request.app.bet_data_worker.delete_record(idn)
