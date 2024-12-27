from . import colour_printer as printer
from .log_levels import LogLevel
import datetime

DefaultLogLevel: LogLevel = LogLevel.INFO

CurrentLogLevel: LogLevel = DefaultLogLevel

LogFile = "logs.log"


def use_timestamped_log_file(use_timestamped_log_file: bool = False):
    global LogFile

    if use_timestamped_log_file:
        LogFile = f"logs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    else:
        LogFile = "logs.log"


def initialise_log_file():
    """Clear the log file at the start of each run."""
    with open(LogFile, "w") as log_file:
        log_file.write("")  # This truncates the file


def set_log_level(log_level: LogLevel):
    global CurrentLogLevel
    CurrentLogLevel = log_level


def format_message(*args) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {' '.join(map(str, args))}"


def strip_ansi(message: str) -> str:
    """Remove ANSI escape sequences from a string."""
    import re

    ansi_escape = re.compile(r"\033\[[0-9;]*m")
    return ansi_escape.sub("", message)


def log_to_file(message: str, colour_code: str):
    # plain_message = strip_ansi(f"\033[{colour_code}m{message}\033[0m")
    with open(LogFile, "a") as file:
        file.write(message + "\n")


def log_to_console_with_colour(message: str, colour_code: str):
    printer.print_coloured(message, colour_code)


def log_message(level: LogLevel, colour_code: str, *args):

    if CurrentLogLevel <= level:
        message = format_message(*args)

        # Log to console with color
        log_to_console_with_colour(message, colour_code)

        # Log to file (with color for tools that render ANSI)
        log_to_file(message, colour_code)


def warning(*args):
    log_message(LogLevel.WARNING, "33", *args)


def error(*args):
    log_message(LogLevel.ERROR, "31", *args)


def info(*args):
    log_message(LogLevel.INFO, "36", *args)


def debug(*args):
    log_message(LogLevel.INFO, "90", *args)


def critical(*args):
    log_message(LogLevel.CRITICAL, "91", *args)
