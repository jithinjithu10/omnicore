import time
import uuid

class RuntimeContext:
    def __init__(self, app_name):
        self.app_name = app_name
        self.instance_id = str(uuid.uuid4())
        self.started_at = None
        self.stopped_at = None

    def mark_start(self):
        self.started_at = time.time()

    def mark_stop(self):
        self.stopped_at = time.time()

    def uptime(self):
        if self.stopped_at:
            return self.stopped_at - self.started_at
        return time.time() - self.started_at
