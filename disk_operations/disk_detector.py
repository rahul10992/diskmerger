import os
import logger.logger as log

local_drive_name = {"Macintosh HD"}
recovery_drive_name = {"Recovery"}


def list_drives():
    return next(os.walk("/Volumes"))[1]


def get_external_drive_paths() -> list:
    drives = list_drives()
    log.debug("Detected external drives:")
    drive_paths = []

    for drive in drives:
        if drive in local_drive_name or drive in recovery_drive_name:
            continue

        log.info("Checking: ", drive)
        log.debug("Navigating drive {}".format(drive))
        drive_paths.append(f"/Volumes/{drive}")

    log.info(f"Detected {len(drive_paths)} external drives")
    return drive_paths
