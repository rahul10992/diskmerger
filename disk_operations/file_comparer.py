from enum import IntEnum
from file import File


class FileComparisonStatus(IntEnum):
    # Keep
    DIFFERENT = 0

    # Ignore operation
    SAME_PATH = 1

    # Check and consider deletion.
    SAME_NAME = 2
    SAME_SIZE = 3
    SAME_HASH = 4


def is_same_file(first_file: File, second_file: File):
    # check if the path is the same.
    if first_file.path == second_file.path:
        return FileComparisonStatus.SAME_PATH

    status = FileComparisonStatus.DIFFERENT

    if first_file.name == second_file.name:
        status = FileComparisonStatus.SAME_NAME

        if first_file.size == second_file.size:
            status = FileComparisonStatus.SAME_SIZE

        if first_file.hash == second_file.hash:
            status = FileComparisonStatus.SAME_HASH

    return status
