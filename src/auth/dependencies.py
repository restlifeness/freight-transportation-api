import jwt

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.db import User, ServiceRoles
from src.core.security import JWTService
from src.users.repositories import UserRepo


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_user_by_token(
        token: Annotated[str, Depends(oauth2_scheme)],
        user_repo: Annotated[UserRepo, Depends()]
    ) -> User:
        """
        Get user by token.

        :param token: token
        :return: user
        """
        try:
            payload = JWTService.decode_token(token)
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        user = await user_repo.get_by_id(payload.get("user_id"))
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return user


async def get_manager_by_token(
        user: Annotated[User, Depends(get_user_by_token)]
    ) -> User:
        """
        Get manager by role.

        :param user: user
        :return: manager
        """
        if user.role.name == ServiceRoles.CUSTOMER:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is not manager/admin",
            )
        return user


async def get_admin_by_token(
        user: Annotated[User, Depends(get_user_by_token)]
    ) -> User:
        """
        Get admin by role.

        :param user: user
        :return: admin
        """
        if user.role.name != ServiceRoles.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is not admin",
            )
        return user
