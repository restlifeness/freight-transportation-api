
from fastapi import Depends

from src.db import InsuranceDayRate

from .repositories import InsuranceRepo
from .schemas import InsuranceDayRateCreate


class InsuranceService:
    def __init__(self, insurance_repo: InsuranceRepo = Depends()) -> None:
        self.repo = insurance_repo

    async def create(self, insurance_rates: list[InsuranceDayRateCreate]) -> list[InsuranceDayRate]:
        """
        Create insurance rate.

        :param insurance: insurance data
        :return: insurance rate
        """
        return [
            await self.repo.create(insurance.model_dump())
            for insurance in insurance_rates
        ]