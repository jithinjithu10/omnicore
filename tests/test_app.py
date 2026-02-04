from omnicore.core.app import OmniApp

def test_app_lifecycle():
    app = OmniApp("test")
    app.start()
    assert app.runtime.started_at is not None
    app.stop()
    assert app.runtime.stopped_at is not None
