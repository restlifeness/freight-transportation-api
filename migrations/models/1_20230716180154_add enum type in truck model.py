from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" SET DEFAULT 'ShippingOrderStatuses.CREATED';
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" SET NOT NULL;
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(11) USING "status"::VARCHAR(11);
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(11) USING "status"::VARCHAR(11);
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(11) USING "status"::VARCHAR(11);
        ALTER TABLE "trucks" ALTER COLUMN "status" SET DEFAULT 'TruckStatuses.FREE';
        ALTER TABLE "trucks" ALTER COLUMN "status" SET NOT NULL;
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(6) USING "status"::VARCHAR(6);
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(6) USING "status"::VARCHAR(6);
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(6) USING "status"::VARCHAR(6);
        INSERT INTO roles (id, name, description) VALUES
        (gen_random_uuid(), 'admin', 'Admin role'),
        (gen_random_uuid(), 'manager', 'Manager role'),
        (gen_random_uuid(), 'customer', 'Customer role');
        """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);
        ALTER TABLE "trucks" ALTER COLUMN "status" DROP NOT NULL;
        ALTER TABLE "trucks" ALTER COLUMN "status" DROP DEFAULT;
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);
        ALTER TABLE "trucks" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" DROP NOT NULL;
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" DROP DEFAULT;
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);
        ALTER TABLE "shipping_orders" ALTER COLUMN "status" TYPE VARCHAR(255) USING "status"::VARCHAR(255);"""
