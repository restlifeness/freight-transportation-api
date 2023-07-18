
from enum import Enum


class ServiceRoles(Enum):
    """Enum for service roles."""
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"


class CargoTypes(Enum):
    """Enum for cargo types."""
    DANGEROUS = "dangerous"
    PERISHABLE = "perishable"
    GENERAL = "general"


class ShippingOrderStatuses(Enum):
    """Enum for shipping order statuses."""
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELED = "canceled"


class TruckStatuses(Enum):
    """Enum for truck statuses."""
    FREE = "free"
    BUSY = "busy"
    BROKEN = "broken"
