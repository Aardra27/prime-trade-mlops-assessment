import yaml
import os


def load_config(config_path):
    """
    Load and validate YAML configuration.
    """

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise ValueError("Config file is empty.")

    required = ["seed", "window", "version"]

    for key in required:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")

    return config