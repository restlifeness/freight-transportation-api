
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr 

from src.roles.schemas import UserRole


class UserBase(BaseModel):
    """ User base schema. """
    email: EmailStr = Field(..., example="example@gmail.ru", description="User email")
    first_name: str = Field(..., example="John", description="User first name")
    last_name: str = Field(..., example="Doe", description="User last name")


class UserCreate(UserBase):
    """ User create schema. """
    password: str = Field(..., example="password", description="User password", exclude=True)


class UserResponse(UserBase):
    """ User response schema. """
    id: UUID = Field(..., example="e4b6e4e8-0b7c-4f4f-8b9f-7e2d0d9e0c0a", description="User id")

    class Config:
        from_attributes = True


class UserWithRoleResponse(UserResponse):
    """ User with role response schema. """
    role: UserRole = Field(..., description="User role")
