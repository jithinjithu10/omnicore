from omnicore.core.app import OmniApp
from omnicore.modules.health import HealthModule

app = OmniApp("basic-app")
health = HealthModule()

app.lifecycle.register(health)

app.start()
print(health.check())
app.stop()
