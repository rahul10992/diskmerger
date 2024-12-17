import os

import logger.logger
from logger import logger as log
from logger.log_levels import LogLevel

directory_to_ignore = {".Spotlight-V100"}
files_to_ignore = {".DS_Store"}


def main():
    path = "/Users/rahul/Desktop/repo/RiderProjects/Sandbox/Sandbox/obj"
    file_names = {}
    duplicate_file_count = 0
    skipped_file_count = 0

    logger.logger.set_log_level(log_level=LogLevel.INFO)

    # for drive_path in disk.get_external_drive_paths():
    #     parse_directory(
    #         drive_path, file_names, duplicate_file_count, skipped_file_count
    #     )

    # Testing:
    parse_directory(path, file_names, duplicate_file_count, skipped_file_count)

    print(
        "Found {} files".format(len(file_names)),
        "Duplicate files: {}".format(duplicate_file_count),
        "Skipped Dirs: {}".format(skipped_file_count),
    )


def parse_directory(path, file_names, duplicate_file_count, skipped_file_count):
    if not os.path.exists(path):
        raise FileNotFoundError("Directory ", path, " Does not exist")

    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(os.path.join(path, file)):
            extension = file.split(".")[-1]
            log.debug(file, "extension:", extension)
            if file in file_names:
                log.error(
                    "[DUPLICATE] ",
                    file,
                    " existing path: ",
                    file_names[file],
                    " the other path: ",
                    os.path.join(path, file),
                )
                duplicate_file_count += 1
            else:
                log.debug("Adding file: ", file)
                file_names[file] = os.path.join(path, file)
        else:
            log.debug("\nParsing Directory: ", os.path.join(path, file), "\n")
            if not file.startswith("."):
                parse_directory(
                    os.path.join(path, file),
                    file_names,
                    duplicate_file_count,
                    skipped_file_count,
                )
            else:
                log.warning("Skipping {} because it seems to be hidden".format(file))
                skipped_file_count += 1

    log.debug("\nFinished parsing ", os.path.join(path))


if __name__ == "__main__":
    main()
