
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

from src.db import CargoTypes, ShippingOrderStatuses
from src.users.schemas import UserResponse
from src.insurance.schemas import InsuranceDayRateResponse


class ShippingOrderBase(BaseModel):
    description: Optional[str] = Field(None, description="Order description")
    weight: Optional[float] = Field(None, description="Order weight")
    cargo_type: Optional[CargoTypes] = Field(None, description="Cargo type")
    pickup_address: Optional[str] = Field(None, description="Pickup address")
    delivery_address: Optional[str] = Field(None, description="Delivery address")
    include_insurance: bool = Field(False, description="Does the order include insurance")


class ShippingOrderCreate(ShippingOrderBase):
    pass


class ShippingOrderResponse(ShippingOrderBase):
    id: UUID = Field(..., example="e4b6e4e8-0b7c-4f4f-8b9f-7e2d0d9e0c0a", description="Order id")
    status: ShippingOrderStatuses = Field(..., example=ShippingOrderStatuses.CREATED, description="Order status")
    insurance_day_rate: Optional[InsuranceDayRateResponse] = Field(None, description="Order insurance day rate")
    customer: UserResponse = Field(..., description="Order customer")

    class Config:
        from_attributes = True
