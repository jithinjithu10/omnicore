import os
import yaml

class ConfigLoader:
    def __init__(self, path="config.yaml", overrides=None):
        self.path = path
        self.overrides = overrides or {}

    def load(self):
        config = {}
        try:
            with open(self.path) as f:
                config = yaml.safe_load(f) or {}
        except FileNotFoundError:
            pass

        for key, value in os.environ.items():
            if key.startswith("OMNICORE_"):
                config[key[9:].lower()] = value

        config.update(self.overrides)
        return config
