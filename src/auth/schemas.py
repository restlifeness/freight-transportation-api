
from typing import Optional

from fastapi import Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, EmailStr


class TokenResponse(BaseModel):
    """ Token response schema. """
    token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
    token_type: Optional[str] = Field("bearer", example="bearer")


class OAuth2PasswordRequestFormEmail(OAuth2PasswordRequestForm):
    def __init__(
        self,
        email: EmailStr = Form(...),
        password: str = Form(...),
        scope: Optional[str] = Form(""),
        grant_type: Optional[str] = Form(None),
        client_id: Optional[str] = Form(None),
        client_secret: Optional[str] = Form(None),
    ):
        self.email = email
        super().__init__(
            grant_type=grant_type,
            username=email,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )
