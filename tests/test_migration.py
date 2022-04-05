from alembic import command

from app.commands import reset_db
from app.migration import get_config, run_upgrade


def test_upgrade_all():
    reset_db()
    run_upgrade()


def test_downgrade():
    alembic_cfg = get_config()
    command.downgrade(alembic_cfg, "base")
