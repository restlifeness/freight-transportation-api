from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "shipping_orders" ADD "include_insurance" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "shipping_orders" ADD "price" DOUBLE PRECISION;
        ALTER TABLE "shipping_orders" ADD "insurance_rate_id" UUID;
        ALTER TABLE "shipping_orders" ADD CONSTRAINT "fk_shipping_insuranc_ce4fae3f" FOREIGN KEY ("insurance_rate_id") REFERENCES "insurance_day_rates" ("id") ON DELETE SET NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "shipping_orders" DROP CONSTRAINT "fk_shipping_insuranc_ce4fae3f";
        ALTER TABLE "shipping_orders" DROP COLUMN "include_insurance";
        ALTER TABLE "shipping_orders" DROP COLUMN "price";
        ALTER TABLE "shipping_orders" DROP COLUMN "insurance_rate_id";"""
