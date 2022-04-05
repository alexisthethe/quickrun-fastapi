import yaml

from app.database import engine, meta
from app.main import app
from app.migration import run_upgrade


def generate_spec_yaml(file: str = "openapi.yaml") -> None:
    """Generate the OpenAPI spec and save it into a file in yaml format"""
    spec = app.openapi()
    with open(file, "w", encoding="UTF-8") as outfile:
        yaml.dump(spec, outfile, default_flow_style=False, sort_keys=False)


def erase_db():
    with engine.connect():
        meta.reflect(engine)
        meta.drop_all(engine)


def reset_db():
    erase_db()
    run_upgrade()
