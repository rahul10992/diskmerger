import os
import argparse

import logger.logger
from logger import logger as log
from logger.log_levels import LogLevel
import disk_operations.disk_detector as disk
import disk_operations.disk_cleanup as cleanup


def main():
    logger.logger.use_timestamped_log_file(True)
    logger.logger.initialise_log_file()
    logger.logger.set_log_level(log_level=LogLevel.INFO)

    parser = argparse.ArgumentParser(description="File parser")
    parser.add_argument(
        "--mode",
        choices=["test", "real"],
        default="test",
        required=True,
        help="Mode of operation",
    )
    args = parser.parse_args()

    path = "/Users/rahul/Desktop/repo/RiderProjects/Sandbox"

    if args.mode == "real":
        for drive_path in disk.get_external_drive_paths():
            temp = cleanup.DiskCleanup(drive_path)
            temp.get_status_report()

    else:
        # Testing mode
        temp = cleanup.DiskCleanup(path)
        temp.get_status_report()
        temp.cleanup()
        temp.get_status_report()


if __name__ == "__main__":
    main()
