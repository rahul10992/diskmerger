import os
from logger import logger as log


def main():
    path = "/Users/rahul/Desktop/repo/RiderProjects/Sandbox/Sandbox/obj"
    file_names = {}

    parse_directory(path, file_names)


def parse_directory(path, file_names):
    if not os.path.exists(path):
        raise FileNotFoundError("Directory ", path, " Does not exist")

    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(os.path.join(path, file)):
            extension = file.split(".")[-1]
            log.info(file, "extension:", extension)
            if file in file_names:
                log.error(file, " - already exists [DUPLICATE]")
            else:
                file_names[file] = os.path.join(path, file)
        else:
            log.info("\nParsing Directory: ", os.path.join(path, file), "\n")
            parse_directory(os.path.join(path, file), file_names)

    log.info("\nFinished parsing ", os.path.join(path))


if __name__ == "__main__":
    main()
