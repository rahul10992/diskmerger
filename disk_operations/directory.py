import os
from file import File


class Directory:
    def __init__(self, path):
        self.files = None
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FileNotFoundError(f"Directory does not exist: {path}")

        self.name = os.path.basename(path)
        self.path = path

    @property
    def files(self):
        if self.files is None:
            files = os.listdir(self.path)
            for file in files:
                self._files.append(File(os.path.join(self.path, file)))

        return self._files

    @files.setter
    def files(self, value):
        self._files = value
