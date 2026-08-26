"""
Funções relacionadas aos tokens JWT.
"""

from datetime import (
    datetime,
    timedelta,
    timezone,
)

import jwt

from app.core.config import settings


ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    subject: str,
    role: str,
) -> str:
    """
    Cria um access token JWT.
    """

    expires_at = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {

        "sub": subject,

        "role": role,

        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )