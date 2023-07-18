
from typing import Annotated
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status

from src.auth import get_manager_by_token

from .repositories import InsuranceRepo
from .schemas import InsuranceDayRateResponse, InsuranceDayRateCreate


insurance_router = APIRouter(
    tags=["insurance"],
    prefix="/insurance",
    dependencies=[Depends(get_manager_by_token)],
)


@insurance_router.get("/rates", response_model=list[InsuranceDayRateResponse])
async def get_insurance_rates(
    start_date: date,
    end_date: date,
    insurance_repo: Annotated[InsuranceRepo, Depends()],
) -> list[InsuranceDayRateResponse]:
    """
    Get insurance rates.

    :return: insurance rates
    """
    return await insurance_repo.get_by_period(start_date, end_date)



@insurance_router.post("/rates", status_code=status.HTTP_201_CREATED)
async def get_insurance_rates(
    insurance_rates: list[InsuranceDayRateCreate],
    insurance_repo: Annotated[InsuranceRepo, Depends()],
) -> list[InsuranceDayRateResponse]:
    """
    Update insurance rates.

    :return: insurance rates
    """
    rates = await insurance_repo.create(insurance_rates)
    return rates
