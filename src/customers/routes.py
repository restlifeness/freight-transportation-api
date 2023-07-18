
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from src.db import User, ServiceRoles
from src.roles.services import RoleService
from src.auth import get_user_by_token

from .schemas import CustomerCreate, CustomerResponse
from .services import CustomerService
from .repositories import CustomerRepo


customers_router = APIRouter(
    tags=["customers"],
)


@customers_router.get("/customers/{customer_id}")
async def get_customer(
    customer_id: str,
    customer_repo: Annotated[CustomerRepo, Depends()],
) -> CustomerResponse:
    """
    Get customer by id.

    :param customer_id: customer id
    :return: customer
    """
    customer = await customer_repo.get_by_id(customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found",
        )
    return customer


@customers_router.post("/customers", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
async def create_customer(
    customer: CustomerCreate,
    user: Annotated[User, Depends(get_user_by_token)],
    customer_service: Annotated[CustomerService, Depends()],
    role_service: Annotated[RoleService, Depends()],
) -> CustomerResponse:
    """
    Create customer for user if not exists.

    :param customer: customer data
    :param user: user
    :param customer_service: customer service
    :param role_service: role service
    :return: customer
    """
    customer = await customer_service.create_customer(user, customer)
    
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer already exists",
        )

    await role_service.grant_role(ServiceRoles.CUSTOMER, user)

    return customer
