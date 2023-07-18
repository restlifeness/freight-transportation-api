
from typing import Optional

from src.core.base.generics import GenericRepo
from src.db import CustomerDetail


class CustomerRepo(GenericRepo[CustomerDetail]):
    def __init__(self) -> None:
        super().__init__(CustomerDetail)

    async def get_by_user_id(self, user_id: str) -> Optional[CustomerDetail]:
        """
        Get customer by user id.

        :param user_id: user id
        :return: customer
        """
        return await CustomerDetail.all().filter(user_id=user_id).select_related("user").first()
