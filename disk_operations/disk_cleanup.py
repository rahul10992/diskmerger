from disk_operations.directory import Directory
from logger import logger as log

import os

FILES_TO_IGNORE = {".DS_Store"}


class DiskCleanup:

    _root: Directory

    # map of directory names all the paths with the same name.
    _all_directories: dict

    _all_symlinks: list

    # map of file names all the paths with the same name.
    _all_files: dict

    _all_empty_directories: list

    def __init__(self, path, dry_run=True):
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FileNotFoundError("Directory ", path, " Does not exist")

        log.info("Starting cleanup for: ", path)
        self._root = Directory(path)
        self.refresh_data_structures()
        self._dry_run = dry_run

    def refresh_data_structures(self):
        log.warning("Refreshing data structures")
        """Recalculate file and directory mappings after deletion."""
        self._all_directories = {}
        self._all_files = {}
        self._all_symlinks = []
        self._all_empty_directories = []
        self.__navigate_directory(self._root)
        log.warning("Finished refreshing data structures")

    def cleanup(self):
        log.info("Starting cleanup")

        self.delete_duplicate_files()
        log.warning("Finished deleting duplicate files")

        self.refresh_data_structures()
        prev_empty_directory_count = len(self._all_empty_directories)
        while prev_empty_directory_count != len(self._all_empty_directories):
            prev_empty_directory_count = len(self._all_empty_directories)
            self.delete_empty_directories()
            self.refresh_data_structures()

    def delete_empty_directories(self):

        for directory in self._all_empty_directories:
            message = ""
            if self._dry_run:
                message = "[DRY RUN]"
            message += "Deleting empty directory: " + directory.path
            log.warning(message)

            if not self._dry_run:
                os.rmdir(directory.path)

    def delete_duplicate_files(self):
        log.warning("Deleting duplicate files")

        for file_name, file_list in self._all_files.items():
            if len(file_list) > 1:
                log.warning(f"Processing duplicate files: {file_name}")

                # Compare files by their hash
                hashes = {}
                for file in file_list:
                    file_hash = file.hash
                    if file_hash not in hashes:
                        hashes[file_hash] = []
                    hashes[file_hash].append(file)

                # Delete duplicates within each hash group
                for file_hash, files_with_same_hash in hashes.items():
                    if len(files_with_same_hash) > 1:
                        # Sort by path length (longer paths first)
                        files_with_same_hash.sort(
                            key=lambda f: len(f.path), reverse=True
                        )

                        # Keep the first file, delete the rest
                        for duplicate_file in files_with_same_hash[1:]:
                            message = ""
                            if self._dry_run:
                                message = "[DRY RUN]"
                            message += f"Deleting duplicate file: {duplicate_file.path}"
                            log.warning(message)
                            if not self._dry_run:
                                os.remove(duplicate_file.path)

        log.warning("finished deleting duplicate files")

    def get_status_report(self):
        log.warning("==========Dupe Dirs==========")
        for dir_name, dir_list in self._all_directories.items():
            dupe_count = len(dir_list)
            if dupe_count > 1:
                log.error(
                    "Duplicate directory: ", dir_name, "number of dupes: ", dupe_count
                )
        log.warning("==============================")

        log.warning("***********Dupe Files***********")
        for file_name, file_list in self._all_files.items():
            dupe_count = len(file_list)
            if dupe_count > 1:
                print("Duplicate file: ", file_name, "number of dupes: ", dupe_count)
        log.warning("********************************")

        log.warning("``````Empty Directories``````")
        log.warning("Empty Directories: ", len(self._all_empty_directories))
        for directory in self._all_empty_directories:
            log.warning("Empty Directory: ", directory.path)
        log.warning("`````````````````````````````")

        log.warning("``````Symbolic Links``````")
        log.warning("Number of symbolic links: ", len(self._all_symlinks))
        for symlink in self._all_symlinks:
            log.warning("Symlink: ", symlink.path)
        log.warning("`````````````````````````")

    def __navigate_directory(self, directory):
        if directory.is_empty:
            self._all_empty_directories.append(directory)
        else:
            for file in directory.files:
                if os.path.islink(file.path):
                    self._all_symlinks.append(file)
                else:
                    if not self._all_files.get(file.name):
                        self._all_files[file.name] = []
                    self._all_files[file.name].append(file)

            for sub_directory in directory.directories:
                if not self._all_directories.get(sub_directory.name):
                    self._all_directories[sub_directory.name] = []
                self._all_directories[sub_directory.name].append(sub_directory)

                # Recursively navigate subdirectories
                self.__navigate_directory(sub_directory)
