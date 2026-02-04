import json
from omnicore.modules.base import Module

class ConfigModule(Module):
    def __init__(self, path="config.json"):
        super().__init__("config")
        self.path = path
        self.config = {}

    def start(self):
        try:
            with open(self.path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}
