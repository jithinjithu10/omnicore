
import asyncio
from omnicore.core.lifecycle import LifecycleManager
from omnicore.core.container import ServiceContainer
from omnicore.core.runtime import RuntimeContext
from omnicore.modules.registry import ModuleRegistry
from omnicore.plugins.loader import PluginLoader

class OmniApp:
    def __init__(self, name: str):
        self.name = name
        self.container = ServiceContainer()
        self.lifecycle = LifecycleManager()
        self.runtime = RuntimeContext(name)
        self.modules = ModuleRegistry()
        self.plugins = PluginLoader()

    def add_module(self, module):
        self.modules.register(module)
        self.lifecycle.register(module)

    def start(self):
        self.runtime.mark_start()
        self.plugins.load(self)
        asyncio.run(self.lifecycle.start_all())

    def stop(self):
        asyncio.run(self.lifecycle.stop_all())
        self.runtime.mark_stop()
