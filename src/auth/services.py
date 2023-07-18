
from typing import Annotated
from fastapi import Depends, HTTPException, status
from werkzeug.security import check_password_hash, generate_password_hash

from src.db import User
from src.core.security import JWTService
from src.users.repositories import UserRepo
from src.users.schemas import UserCreate

from .schemas import OAuth2PasswordRequestFormEmail, TokenResponse


class AuthService:
    def __init__(self, user_repo: Annotated[UserRepo, Depends()]) -> None:
        self.user_repo = user_repo

    async def auth_user(self, user_data: OAuth2PasswordRequestFormEmail) -> User:
        """
        Authenticate user.

        :param user_data: user data
        :return: token
        """
        user = await self.user_repo.get_by_email_with_role(user_data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User with this email does not exist",
            )

        if not check_password_hash(user.hashed_password, user_data.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect password",
            )

        return user

    async def create_user(self, user_data: UserCreate) -> User:
        """
        Create user.
        
        :param user_data: user data
        :return: user
        """
        user = await self.user_repo.get_by_email_with_role(user_data.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists",
            )

        user = await self.user_repo.create(
            **user_data.model_dump(),
            hashed_password=generate_password_hash(user_data.password),
        )
        
        return user

    def generate_token(self, user: User) -> TokenResponse:
        """
        Generate token.

        :param user: user
        :return: token
        """
        payload = {
            "user_id": str(user.id),
            "role": user.role.name if user.role else None,
        }
        token_str = JWTService.encode_token(payload)
        return TokenResponse(token=token_str)
