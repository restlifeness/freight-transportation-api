
from uuid import UUID
from pydantic import BaseModel, Field

from src.users.schemas import UserWithRoleResponse


class CustomerBase(BaseModel):
    company_name: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=255)
    address: str = Field(..., max_length=255)


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: UUID = Field(..., example="e4b6e4e8-0b7c-4f4f-8b9f-7e2d0d9e0c0a", description="Customer id")
    user: UserWithRoleResponse = Field(..., description="Customer user")

    class Config:
        from_attributes = True
