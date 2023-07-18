
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from src.db import User
from src.auth import get_user_by_token, get_manager_by_token

from .repositories import OrderRepo
from .services import OrderService
from .schemas import ShippingOrderResponse, ShippingOrderCreate


orders_router = APIRouter(
    tags=["orders"],
)


@orders_router.get("/orders")
async def get_orders(
    user: Annotated[User, Depends(get_manager_by_token)],
    repo: Annotated[OrderRepo, Depends()],
    offset: int = 0,
    limit: int = 10,
) -> list[ShippingOrderResponse]:
    """
    Get orders.

    :return: orders
    """
    return await repo.filter_and_paginate_with_relations(
        offset=offset,
        limit=limit,
    )


@orders_router.get("/orders/{order_id}")
async def get_order(
    order_id: UUID,
    user: Annotated[User, Depends(get_user_by_token)],
    repo: Annotated[OrderRepo, Depends()]
) -> ShippingOrderResponse:
    """
    Get order.

    :return: order
    """
    return await repo.get(order_id)


@orders_router.get("users/{user_id}/orders")
async def get_orders_by_customer(
    user_id: UUID,
    user: Annotated[User, Depends(get_user_by_token)],
    repo: Annotated[OrderRepo, Depends()],
    offset: int = 0,
    limit: int = 10,
) -> list[ShippingOrderResponse]:
    """
    Get orders.

    :return: orders
    """
    return await repo.get_by_user_with_relations(
        offset=offset,
        limit=limit,
        user_id=user_id,
    )


@orders_router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: ShippingOrderCreate,
    user: Annotated[User, Depends(get_user_by_token)],
    service: Annotated[OrderService, Depends()],
    ) -> ShippingOrderResponse:
    """
    Create order.

    :param order_data: order fields
    :param user: user
    :param service: order service
    :return: order
    """
    return await service.create_order(user, order_data)


@orders_router.put("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def update_order(
    order_id: UUID,
    user: Annotated[User, Depends(get_user_by_token)],
    order_data: ShippingOrderCreate,
    service: Annotated[OrderService, Depends()],
) -> ShippingOrderResponse:
    """
    Update order.

    :return: order
    """
    return await service.update_order(order_id, user, order_data)
