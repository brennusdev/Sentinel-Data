"""
Sentinel Data
---------------
Autenticação das requisições utilizando JWT.
"""

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import (
    OAuth2PasswordBearer,
)

import jwt

from app.core.config import settings


# Define de onde o FastAPI deve obter
# o Bearer Token.
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> dict:
    """
    Valida o JWT e retorna as informações
    do usuário autenticado.
    """

    try:

        # Decodifica e valida o JWT.
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )

        # Identificação do usuário.
        user_id = payload.get("sub")

        # Papel do usuário.
        role = payload.get("role")

        # Se não houver identificação,
        # o token é considerado inválido.
        if not user_id:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )

        return {
            "user_id": user_id,
            "role": role,
        }

    except jwt.PyJWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )