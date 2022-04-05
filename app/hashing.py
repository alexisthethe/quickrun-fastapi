from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(plain_pass: str, hashed_pass: str):
        return pwd_ctx.verify(plain_pass, hashed_pass)
