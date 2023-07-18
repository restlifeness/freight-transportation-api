from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "roles" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(8) NOT NULL  DEFAULT 'customer',
    "description" TEXT
);
COMMENT ON COLUMN "roles"."name" IS 'ADMIN: admin\nMANAGER: manager\nCUSTOMER: customer';
CREATE TABLE IF NOT EXISTS "trucks" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "license_plate" VARCHAR(255) NOT NULL UNIQUE,
    "model" VARCHAR(255),
    "capacity" DOUBLE PRECISION,
    "status" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "first_name" VARCHAR(255),
    "last_name" VARCHAR(255),
    "role_id" UUID REFERENCES "roles" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "customer_details" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "company_name" VARCHAR(255),
    "phone_number" VARCHAR(255),
    "address" TEXT,
    "user_id" UUID NOT NULL UNIQUE REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "shipping_orders" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "description" TEXT,
    "status" VARCHAR(255),
    "weight" DOUBLE PRECISION,
    "cargo_type" VARCHAR(10),
    "pickup_address" TEXT,
    "delivery_address" TEXT,
    "customer_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "truck_id" UUID REFERENCES "trucks" ("id") ON DELETE SET NULL
);
COMMENT ON COLUMN "shipping_orders"."cargo_type" IS 'DANGEROUS: dangerous\nPERISHABLE: perishable\nGENERAL: general';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
