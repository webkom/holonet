class ServiceManager:
    def __init__(self):
        self._backends = {}

    def add(self, name, cls):
        self._backends[name] = cls

    def get(self, name):
        return self._backends.get(name, None)

    def items(self):
        return self._backends.items()

    @property
    def choices(self):
        return [(v, v) for v in sorted(self._backends.keys())]

    def keys(self):
        return list(self._backends.keys())
