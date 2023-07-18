from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "insurance_day_rates" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "rate" DOUBLE PRECISION,
    "date" DATE,
    "cargo_type" VARCHAR(10)
);
COMMENT ON COLUMN "insurance_day_rates"."cargo_type" IS 'DANGEROUS: dangerous\nPERISHABLE: perishable\nGENERAL: general';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "insurance_day_rates";"""
