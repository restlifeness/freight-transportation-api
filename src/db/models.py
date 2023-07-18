
from tortoise import fields
from tortoise.models import Model

from .enums import CargoTypes, ServiceRoles, ShippingOrderStatuses, TruckStatuses


class TimestampMixin(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(Model):
    id = fields.UUIDField(pk=True)

    class Meta:
        abstract = True


class Role(UUIDMixin, TimestampMixin):
    name = fields.CharEnumField(ServiceRoles, default=ServiceRoles.CUSTOMER)
    description = fields.TextField(null=True)

    class Meta:
        table = "roles"


class User(UUIDMixin, TimestampMixin):
    email = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)

    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)

    role = fields.ForeignKeyField("models.Role", related_name="users", null=True, on_delete=fields.CASCADE)

    class Meta:
        table = "users"


class CustomerDetail(UUIDMixin, TimestampMixin):
    user = fields.OneToOneField("models.User", related_name="customer_details", on_delete=fields.CASCADE)
    company_name = fields.CharField(max_length=255, null=True)
    phone_number = fields.CharField(max_length=255, null=True)
    address = fields.TextField(null=True)

    class Meta:
        table = "customer_details"


class ShippingOrder(UUIDMixin, TimestampMixin):
    customer = fields.ForeignKeyField("models.User", related_name="shipping_orders", on_delete=fields.CASCADE)
    truck = fields.ForeignKeyField("models.Truck", related_name="shipping_orders", null=True, on_delete=fields.SET_NULL)
    description = fields.TextField(null=True)
    status = fields.CharEnumField(ShippingOrderStatuses, default=ShippingOrderStatuses.CREATED)

    weight = fields.FloatField(null=True)
    cargo_type = fields.CharEnumField(CargoTypes, null=True)

    pickup_address = fields.TextField(null=True)
    delivery_address = fields.TextField(null=True)

    price = fields.FloatField(null=True)
    include_insurance = fields.BooleanField(default=False)
    insurance_rate = fields.ForeignKeyField(
        "models.InsuranceDayRate", 
        related_name="shipping_orders", 
        null=True, 
        on_delete=fields.SET_NULL
    )

    class Meta:
        table = "shipping_orders"


class Truck(UUIDMixin, TimestampMixin):
    license_plate = fields.CharField(max_length=255, unique=True)
    model = fields.CharField(max_length=255, null=True)
    capacity = fields.FloatField(null=True)
    status = fields.CharEnumField(TruckStatuses, default=TruckStatuses.FREE)

    class Meta:
        table = "trucks"


class InsuranceDayRate(UUIDMixin, TimestampMixin):
    rate = fields.FloatField(null=True)
    date = fields.DateField(null=True)
    cargo_type = fields.CharEnumField(CargoTypes, null=True)

    class Meta:
        table = "insurance_day_rates"
