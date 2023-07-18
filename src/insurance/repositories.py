
from datetime import date

from src.db import InsuranceDayRate

from src.core.base.generics import GenericRepo
from src.db import InsuranceDayRate


class InsuranceRepo(GenericRepo[InsuranceDayRate]):
    def __init__(self) -> None:
        super().__init__(InsuranceDayRate)

    async def get_by_period(self, start_date: date, end_date: date) -> list[InsuranceDayRate]:
        """
        Get insurance rates by period.

        :param start_date: start date
        :param end_date: end date
        :return: insurance rates
        """
        return await InsuranceDayRate.all().filter(
            date__gte=start_date,
            date__lte=end_date,
        ).order_by("date").all()
