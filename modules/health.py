from omnicore.modules.base import Module

class HealthModule(Module):
    def __init__(self):
        super().__init__("health")
        self.status = "INIT"

    def start(self):
        self.status = "RUNNING"

    def stop(self):
        self.status = "STOPPED"

    def check(self):
        return {"status": self.status}
