import logging
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app import schemas
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class NotAuthorized(Exception):
    """Exception when a request does not have the right login"""

    def __init__(self, username: str = ""):
        msg = f"Not authorized (user: {username})"
        logging.exception(f"Exception {self.__class__.__name__}: {msg}")
        super().__init__(msg)


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(plain_pass: str, hashed_pass: str):
        return pwd_ctx.verify(plain_pass, hashed_pass)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise NotAuthorized(email)
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise NotAuthorized(email)
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)
