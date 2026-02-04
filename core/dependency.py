class DependencyGraph:
    def __init__(self):
        self.graph = {}

    def add(self, name, depends_on=None):
        self.graph[name] = depends_on or []

    def resolve(self):
        resolved = []
        unresolved = []

        def visit(node):
            if node in resolved:
                return
            if node in unresolved:
                raise RuntimeError("Circular dependency detected")
            unresolved.append(node)
            for dep in self.graph.get(node, []):
                visit(dep)
            unresolved.remove(node)
            resolved.append(node)

        for node in self.graph:
            visit(node)

        return resolved
