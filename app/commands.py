import yaml

from app.main import app


def generate_spec_yaml(file: str = "openapi.yaml") -> None:
    """Generate the OpenAPI spec and save it into a file in yaml format"""
    spec = app.openapi()
    with open(file, "w", encoding="UTF-8") as outfile:
        yaml.dump(spec, outfile, default_flow_style=False, sort_keys=False)
