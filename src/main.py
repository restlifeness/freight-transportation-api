import config
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.auth import auth_router
from src.customers import customers_router
from src.insurance import insurance_router
from src.orders import orders_router

from src.core.settings import PostgresDrivers, get_settings


settings = get_settings()

ASYNC_POSTGRES_URI = settings.get_db_uri()


app = FastAPI(
    debug=settings.DEBUG,
)


register_tortoise(
    app,
    db_url=ASYNC_POSTGRES_URI,
    modules={"models": ["src.db.models"]},
    generate_schemas=False,
)


app.include_router(auth_router)
app.include_router(customers_router)
app.include_router(insurance_router)
app.include_router(orders_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    main()
