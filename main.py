import os
from logger import logger as log

local_drive_name = {"Macintosh HD"}
directory_to_ignore = {".Spotlight-V100"}
files_to_ignore = {".DS_Store"}


def main():
    path = "/Users/rahul/Desktop/repo/RiderProjects/Sandbox/Sandbox/obj"
    file_names = {}
    duplicate_file_count = 0
    skipped_file_count = 0

    # parse_directory(path, file_names)
    drives = list_drives()
    print("Detected external drives:")
    for drive in drives:
        if drive in local_drive_name:
            continue
        log.debug("Navigating drive {}".format(drive))
        drive_path = f"/Volumes/{drive}"
        parse_directory(
            drive_path, file_names, duplicate_file_count, skipped_file_count
        )

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
            # log.debug(file, "extension:", extension)
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
                file_names[file] = os.path.join(path, file)
        else:
            # log.debug("\nParsing Directory: ", os.path.join(path, file), "\n")
            if not file.startswith("."):
                parse_directory(
                    os.path.join(path, file),
                    file_names,
                    duplicate_file_count,
                    skipped_file_count,
                )
            else:
                log.debug("Skipping {} because it seems to be hidden".format(file))
                skipped_file_count += 1

    # log.debug("\nFinished parsing ", os.path.join(path))


def list_drives():
    # This command lists all volumes in /Volumes, which is where macOS mounts external drives
    return next(os.walk("/Volumes"))[1]


def count_files_in_drive(drive_path):
    file_count = 0
    for root, dirs, files in os.walk(drive_path):
        file_count += len(files)
    return file_count


if __name__ == "__main__":
    main()
