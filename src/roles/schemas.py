
from uuid import UUID
from pydantic import BaseModel, Field


class UserRole(BaseModel):
    """ User role schema. """
    id: UUID = Field(..., example="e4b6e4e8-0b7c-4f4f-8b9f-7e2d0d9e0c0a", description="User role id")
    name: str = Field(..., example="CUSTOMER", description="User role name")

    class Config:
        from_attributes = True
