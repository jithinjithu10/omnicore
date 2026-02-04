import importlib.metadata

class PluginLoader:
    ENTRYPOINT = "omnicore.plugins"

    def load(self, app):
        for entry in importlib.metadata.entry_points().get(self.ENTRYPOINT, []):
            plugin_cls = entry.load()
            plugin = plugin_cls()
            plugin.register(app)
