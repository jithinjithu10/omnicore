class LifecycleManager:
    def __init__(self):
        self.components = []

    def register(self, component):
        self.components.append(component)

    def start_all(self):
        for c in self.components:
            if hasattr(c, "start"):
                c.start()

    def stop_all(self):
        for c in reversed(self.components):
            if hasattr(c, "stop"):
                c.stop()
