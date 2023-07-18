import sys

from tortoise.contrib.fastapi import register_tortoise

from pathlib import Path
sys.path.append(str(Path.cwd()))

from src.core.settings import get_settings, PostgresDrivers


settings = get_settings()

POSTGRES_URI = settings.get_db_uri()


TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URI},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

INITIAL_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': settings.POSTGRES_HOST,
                'port': settings.POSTGRES_PORT,
                'user': settings.POSTGRES_USER,
                'password': settings.POSTGRES_PASSWORD,
                'database': settings.POSTGRES_DB,
            }
        }
    }
}

CORS_ORIGINS = (
    "http://localhost",
)
