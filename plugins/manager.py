import traceback

class PluginManager:
    def __init__(self):
        self.loaded = {}

    def load_plugin(self, plugin_cls, app):
        try:
            plugin = plugin_cls()
            plugin.register(app)
            self.loaded[plugin.name] = plugin
        except Exception as e:
            print(f"[PLUGIN ERROR] {plugin_cls}: {e}")
            traceback.print_exc()

    def unload(self, name):
        if name in self.loaded:
            del self.loaded[name]
