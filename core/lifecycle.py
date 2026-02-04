import inspect
import asyncio

class LifecycleManager:
    def __init__(self):
        self.components = []

    def register(self, component):
        self.components.append(component)

    async def start_all(self):
        for c in self.components:
            if hasattr(c, "start"):
                if inspect.iscoroutinefunction(c.start):
                    await c.start()
                else:
                    c.start()

    async def stop_all(self):
        for c in reversed(self.components):
            if hasattr(c, "stop"):
                if inspect.iscoroutinefunction(c.stop):
                    await c.stop()
                else:
                    c.stop()
