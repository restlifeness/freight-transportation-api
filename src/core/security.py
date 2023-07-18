import jwt

from datetime import datetime, timedelta

from .settings import get_settings


settings = get_settings()


class JWTService:
    @staticmethod
    def encode_token(payload: dict) -> str:
        """
        Encode payload dict and return JWT token.
        
        :param payload: payload dict
        :return: JWT token
        """
        expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
        payload['exp'] = expire
        return jwt.encode(
            payload,
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )

    @staticmethod
    def decode_token(token: str) -> dict:
        """
        Decode token and return payload dict.
        
        :param token: JWT token
        :return: payload dict
        """
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
