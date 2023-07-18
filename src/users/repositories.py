
from typing import Optional

from src.core.base.generics import GenericRepo
from src.db import User


class UserRepo(GenericRepo[User]):
    def __init__(self) -> None:
        super().__init__(User)

    async def get_by_email_with_role(self, email: str) -> Optional[User]:
        """
        Get user by email.

        :param email: user email
        :return: user
        """
        return await User.all().filter(email=email).select_related("role").first()

    async def get_by_id_with_role(self, user_id: int) -> Optional[User]:
        """
        Get user by id with role.

        :param user_id: user id
        :return: user
        """
        return await User.all().filter(id=user_id).select_related("role").first()
