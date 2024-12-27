import os
import hashlib


class File:
    def __init__(self, path):
        self.size = None
        self.hash = None
        if not os.path.exists(path):
            raise FileNotFoundError(f"File does not exist: {path}")

        self.name = os.path.basename(path)
        self.path = path

    @property
    def size(self):
        if self.size is None:
            self._size = os.path.getsize(self.path)
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def hash(self):
        if self.hash is None:
            self._hash = hashlib.sha256(open(self.path, "rb").read()).hexdigest()
        return self._hash

    @hash.setter
    def hash(self, value):
        self._hash = value
