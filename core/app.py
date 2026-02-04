
from omnicore.core.lifecycle import LifecycleManager
from omnicore.core.container import ServiceContainer
from omnicore.core.runtime import RuntimeContext
import asyncio

class OmniApp:
    def __init__(self, name: str):
        self.name = name
        self.container = ServiceContainer()
        self.lifecycle = LifecycleManager()
        self.runtime = RuntimeContext(name)

def start(self):
    self.runtime.mark_start()
    asyncio.run(self.lifecycle.start_all())

def stop(self):
    asyncio.run(self.lifecycle.stop_all())
    self.runtime.mark_stop()
