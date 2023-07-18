
from typing import Optional

from src.core.base.generics import GenericRepo
from src.db import Role, ServiceRoles


class RoleRepo(GenericRepo[Role]):
    def __init__(self) -> None:
        super().__init__(Role)

    async def get_by_role_type(self, role: ServiceRoles) -> Optional[Role]:
        """
        Get role by type.

        :param role: role type
        :return: role
        """
        return await Role.all().filter(role=role).first()

    