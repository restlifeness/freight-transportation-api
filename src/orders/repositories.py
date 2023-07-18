
from src.core.base.generics import GenericRepo
from src.db import ShippingOrder


class OrderRepo(GenericRepo[ShippingOrder]):
    def __init__(self) -> None:
        self.relations = (
            "truck",
            "customer",
            "insurance_rate",
        )
        super().__init__(ShippingOrder)

    async def get_by_user_with_relations(
        self, 
        offset: int,
        skip: int,
        user_id: int
    ):
        """
        Get orders by user with relations.
        
        :param user_id: user id
        :return: orders
        """
        return await (
            self.Model
            .filter(customer_id=user_id)
            .select_related(*self.relations)
            .offset(offset)
            .limit(skip)
            .all()
        )

    async def filter_and_paginate_with_relations(
        self,
        offset: int,
        limit: int,
        **kwargs
    ):
        """
        Filter and paginate orders with relations.
        
        :param offset: offset
        :param limit: limit
        :param select_relations: relations to select
        :param kwargs: filter params
        :return: orders
        """
        return await self.filter_and_paginate(
            offset=offset,
            limit=limit,
            select_relations=self.relations,
            **kwargs
        )
