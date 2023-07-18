
from datetime import date, datetime
from pydantic import BaseModel, Field

from src.db import CargoTypes


class InsuranceDayRateBase(BaseModel):
    rate: float = Field(..., example=0.1, description="Insurance day rate")
    date: str = Field(..., example="2021-01-01", description="Insurance day rate date")
    cargo_type: CargoTypes = Field(..., example=CargoTypes.GENERAL, description="Insurance day rate cargo type")


class InsuranceDayRateCreate(InsuranceDayRateBase):
    pass


class InsuranceDayRateResponse(InsuranceDayRateBase):
    id: str = Field(..., example="e4b6e4e8-0b7c-4f4f-8b9f-7e2d0d9e0c0a", description="Insurance day rate id")

    class Config:
        from_attributes = True
