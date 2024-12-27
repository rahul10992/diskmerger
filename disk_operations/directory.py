import os

from disk_operations.file import File


class Directory:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError("Directory ", path, " Does not exist")

        if not os.path.isdir(path):
            raise IsADirectoryError("Path is a directory: ", path)

        self._path = path
        self._name = os.path.basename(path)
        self._files = []
        self._directories = []

        self._parse_directory()

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def files(self):
        return self._files

    @property
    def directories(self):
        return self._directories

    @property
    def is_empty(self):
        return len(self._files) == 0 and len(self._directories) == 0

    @staticmethod
    def compare_directories(directory1, directory2):
        if directory1.path == directory2.path:
            raise ValueError("Cannot compare the same directory")

        same_file_count = 0
        diff_file_count = 0

        for file1 in directory1.files:
            for file2 in directory2.files:
                if File.compare(file1, file2):
                    same_file_count += 1
                else:
                    diff_file_count += 1

    IGNORED_FILES = {".DS_Store"}

    def _parse_directory(self):
        files = os.listdir(self.path)
        for file in files:
            if not os.path.isdir(os.path.join(self.path, file)):
                if file in self.IGNORED_FILES:
                    continue
                self._files.append(File(os.path.join(self.path, file)))
            else:
                self._directories.append(Directory(os.path.join(self.path, file)))
