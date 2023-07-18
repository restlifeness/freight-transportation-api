
from typing import TypeVar, NewType, Type, Generic, Optional, Any

from db.models import Model


T = TypeVar("T", bound=Model)
ModelField = NewType("ModelField", str)


class GenericRepo(Generic[T]):
    def __init__(self, model: Type[T]) -> None:
        """
        Generic repository for database models.

        :param model: database model
        """
        self.Model = model

    async def get(self, id: Any) -> Optional[T]:
        """
        Get model by id.

        :param id: model id
        :return: model or None
        """
        return await self.Model.get_or_none(id=id)

    async def create(self, **kwargs) -> T:
        """
        Create model.

        :param kwargs: model fields
        :return: created model
        """
        return await self.Model.create(**kwargs)

    async def update(self, model: T, **kwargs) -> T:
        """
        Update model.

        :param model: model to update
        :param kwargs: model fields to update
        :return: updated model
        """
        for key, value in kwargs.items():
            setattr(model, key, value)

        await model.save()

        return model

    async def delete(self, model: T) -> None:
        """
        Delete model.

        :param model: model to delete
        """
        await model.delete()

    async def all(self) -> list[T]:
        """
        Get all models.

        :return: list of models
        """
        return await self.Model.all()

    async def filter(self, **kwargs) -> list[T]:
        """
        Filter models.

        :param kwargs: filter params
        :return: list of models
        """
        return await self.Model.filter(**kwargs)

    async def filter_and_paginate(
        self, 
        offset: int, 
        limit: int,
        select_relations: list[ModelField | str] = None,
        **filters
    ) -> list[T]:
        """
        Paginate and filter models.

        :param page: page number
        :param per_page: models per page
        :param kwargs: filter params
        :return: list of models
        """
        return await (
            self.Model
            .filter(**filters)
            .all()
            .select_related(*select_relations)
            .offset(offset)
            .limit(limit)
        )
