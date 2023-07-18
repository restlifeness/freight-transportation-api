
from typing import Annotated, Optional
from fastapi import Depends

from src.db import User, CustomerDetail, ServiceRoles

from .repositories import CustomerRepo
from .schemas import CustomerCreate


class CustomerService:
    def __init__(self, customer_repo: Annotated[CustomerRepo, Depends()]) -> None:
        self.repo = customer_repo

    async def create_customer(self, user: User, customer: CustomerCreate) -> CustomerDetail | bool:
        """
        Create customer for user if not exists.

        :param customer: customer data
        :return: customer or False
        """
        already_exists = await self.repo.get_by_user_id(user_id=user.id)
        if already_exists:
            return False

        customer = await self.repo.create(
            user=user,
            company_name=customer.company_name,
            phone_number=customer.phone_number,
            address=customer.address,
        )
        return customer
