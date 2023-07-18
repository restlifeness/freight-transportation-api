
from typing import Annotated
from datetime import datetime
from fastapi import Depends, HTTPException, status

from src.db import User, CargoTypes
from src.insurance.repositories import InsuranceRepo

from .repositories import OrderRepo
from .schemas import ShippingOrderCreate


MOCK_CARGO_PRICES = {
    CargoTypes.GENERAL: 100,
    CargoTypes.DANGEROUS: 200,
    CargoTypes.PERISHABLE: 300,
}


class OrderService:
    def __init__(
        self, 
        repo: Annotated[OrderRepo, Depends()],
        insurance_repo: Annotated[InsuranceRepo, Depends()],
    ) -> None:
        self.repo = repo
        self.insurance_repo = insurance_repo

    async def create_order(self, customer: User, order_data: ShippingOrderCreate) -> None:
        """
        Create order.

        :param kwargs: order fields
        """
        price = MOCK_CARGO_PRICES[order_data.cargo_type]

        if order_data.include_insurance:
            insurance_rates = await self.insurance_repo.filter(
                cargo_type=order_data.cargo_type,
                date=datetime.now().date(),
            )
            last_insurance_rate = insurance_rates[0]

            price = price * last_insurance_rate.rate

        return await self.repo.create(
            **order_data.model_dump(),
            price=price,
            insurance_rate=last_insurance_rate,
        )

    async def update_order(
        self, 
        order_id: str, 
        user: User,
        order_data: ShippingOrderCreate
    ) -> None:
        """
        Update order.

        :param order_id: order id
        :param order_data: order fields
        """
        order = await self.repo.get(order_id)
        
        if order.customer.id != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can't update this order",
            )
        
        return await self.repo.update(
            order,
            **order_data.model_dump(),
        )
