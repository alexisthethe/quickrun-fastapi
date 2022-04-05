import os

from alembic import command
from alembic.config import Config

from app.config import settings
from app.database import sqlalchemy_url


def get_config() -> Config:
    script_cfg_file = os.path.join(settings.PROJECT_DIR, "../alembic.ini")
    alembic_cfg = Config(script_cfg_file)
    alembic_cfg.set_main_option("sqlalchemy.url", sqlalchemy_url)
    return alembic_cfg


def run_upgrade() -> None:
    alembic_cfg = get_config()
    command.upgrade(alembic_cfg, "head")
