from file import File
from directory import Directory
from file_comparer import is_same_file, FileComparisonStatus
from logger import logger as log


def compare_directories(first_directory: Directory, second_directory: Directory):
    if (
        first_directory.path == second_directory.path
        and first_directory.name == second_directory.name
    ):
        # ignore same path. return whatever means "its all good"
        return FileComparisonStatus.SAME_PATH

    same_hash_files = []
    same_size_files = []
    same_name_files = []

    if first_directory.name == second_directory.name:
        # check number of files with the same hash
        # check number of files with the same size and name.
        # check number of files with the same name.

        first_dir_files = first_directory.files
        second_dir_files = second_directory.files

        for first_file in first_dir_files:
            for second_file in second_dir_files:
                status = is_same_file(first_file, second_file)
                if status == FileComparisonStatus.SAME_HASH:
                    same_hash_files.append((first_file.path, second_file.path))
                elif status == FileComparisonStatus.SAME_SIZE:
                    same_size_files.append((first_file.path, second_file.path))
                elif status == FileComparisonStatus.SAME_NAME:
                    same_name_files.append((first_file.path, second_file.path))

        log.warning("=================Same DirectoryName report=================")
        log.info(f"The directories {first_directory.path} and {second_directory.path}")
        log.info(
            f"have {len(first_dir_files)} files and {len(second_dir_files)} files respectively.\nFrom these files:"
        )
        log.critical(f"Same Hash files: {len(same_hash_files)}")
        log.warning(f"Same Size files: {len(same_size_files)}")
        log.info(f"Same Name files: {len(same_name_files)}")
        log.warning("===========================================================\n\n")
