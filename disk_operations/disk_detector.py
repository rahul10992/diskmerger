import os
import logger.logger as log

local_drive_name = {"Macintosh HD"}


def list_drives():
    return next(os.walk("/Volumes"))[1]


def get_external_drive_paths() -> list:
    drives = list_drives()
    log.info("Detected external drives:")
    drive_paths = []

    for drive in drives:
        if drive in local_drive_name:
            continue

        log.info("Checking: ", drive)
        log.debug("Navigating drive {}".format(drive))
        drive_paths.append(f"/Volumes/{drive}")

    return drive_paths
