import os
import urllib.parse

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings


def get_sqlalchemy_url() -> str:
    """return the right DB URL for SQLAlchemy according to DB Settings"""
    if settings.DB_TYPE == "sqlite":
        db_file = os.path.join(settings.PROJECT_DIR, f"{settings.DB_NAME}.db")
        return f"sqlite:///{db_file}"
    else:
        name_safe = urllib.parse.quote_plus(settings.DB_NAME)
        user_safe = urllib.parse.quote_plus(settings.DB_USER)
        password_safe = urllib.parse.quote_plus(settings.DB_PASSWORD)
        return f"{settings.DB_TYPE}://{user_safe}:{password_safe}@{settings.DB_HOST}:{settings.DB_PORT}/{name_safe}"


sqlalchemy_url = get_sqlalchemy_url()

engine = create_engine(sqlalchemy_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()
Base = declarative_base(metadata=meta)


def get_db():
    """Init DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
