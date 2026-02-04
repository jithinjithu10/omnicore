class FileSystemExtension:
    def read(self, path):
        with open(path) as f:
            return f.read()

    def write(self, path, data):
        with open(path, "w") as f:
            f.write(data)
