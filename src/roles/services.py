
from typing import Annotated
from fastapi import Depends

from src.db import ServiceRoles, User
from src.users.repositories import UserRepo
from .repositories import RoleRepo


class RoleService:
    def __init__(
        self, 
        role_repo: Annotated[RoleRepo, Depends()],
        user_repo: Annotated[UserRepo, Depends()],
    ) -> None:
        self.repo = role_repo
        self.user_repo = user_repo

    async def grant_role(self, role_type: ServiceRoles, user: User) -> User:
        """
        Grant role to user.

        :param role: role type
        :param user: user
        """
        role = await self.repo.get_by_role_type(role_type)
        return await self.user_repo.update(user, role=role)
