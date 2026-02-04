import os
import socket
import uuid

class InstanceInfo:
    def __init__(self):
        self.instance_id = str(uuid.uuid4())
        self.pid = os.getpid()
        self.host = socket.gethostname()

    def info(self):
        return {
            "instance_id": self.instance_id,
            "pid": self.pid,
            "host": self.host
        }
