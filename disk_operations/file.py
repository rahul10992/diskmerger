import os
import hashlib


class File:
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File does not exist: {path}")

        if os.path.isdir(path):
            raise IsADirectoryError(f"Path is a directory: {path}")

        self._path = path
        self._name = os.path.basename(path)
        self._hash = None
        self._size = os.path.getsize(path)
        # TODO: remove if not needed?
        self._extension = self.name.split(".")[-1]

    @property
    def extension(self):
        return self._extension

    @property
    def size(self):
        return self._size

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    # lazy loading
    @property
    def hash(self):
        if not self._hash:
            hash_function = hashlib.sha256()
            with open(self.path, "rb") as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    hash_function.update(chunk)
            self._hash = hashlib.sha256(open(self.path, "rb").read()).hexdigest()
        return self._hash

    @staticmethod
    def compare(file1, file2):
        return file1.hash == file2.hash
