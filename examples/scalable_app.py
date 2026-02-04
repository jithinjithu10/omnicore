from omnicore.core.app import OmniApp
from omnicore.modules.config import ConfigModule
from omnicore.extensions.filesystem import FileSystemExtension

app = OmniApp("scalable-app")
config = ConfigModule()
fs = FileSystemExtension()

app.lifecycle.register(config)

app.start()
print("Config loaded:", config.config)
fs.write("output.txt", "OmniCore running")
app.stop()
