class Plugin:
    name = "base"

    def register(self, app):
        """
        Called when plugin is loaded.
        App instance is provided for registration.
        """
        raise NotImplementedError
