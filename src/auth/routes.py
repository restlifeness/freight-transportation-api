
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from src.users.schemas import UserCreate

from .services import AuthService
from .schemas import TokenResponse, OAuth2PasswordRequestFormEmail


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post("/login", response_model=TokenResponse) 
async def login(
    form_data: Annotated[OAuth2PasswordRequestFormEmail, Depends()],
    auth_service: Annotated[AuthService, Depends()],
) -> TokenResponse:
    user = await auth_service.auth_user(form_data)
    return auth_service.generate_token(user)


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    auth_service: Annotated[AuthService, Depends()],
) -> TokenResponse:
    user = await auth_service.create_user(user_data)
    return auth_service.generate_token(user)
