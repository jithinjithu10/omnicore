import signal
import sys

class GracefulShutdown:
    def __init__(self, app):
        self.app = app
        signal.signal(signal.SIGTERM, self.exit)
        signal.signal(signal.SIGINT, self.exit)

    def exit(self, signum, frame):
        print(f"Shutting down ({signum})")
        self.app.stop()
        sys.exit(0)
