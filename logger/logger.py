from . import colour_printer as printer
from .log_levels import LogLevel

DefaultLogLevel: LogLevel = LogLevel.INFO

CurrentLogLevel: LogLevel = DefaultLogLevel


def set_log_level(log_level: LogLevel):
    global CurrentLogLevel
    CurrentLogLevel = log_level


def format_message(*args) -> str:
    return " ".join(map(str, args))


def warning(*args):
    if CurrentLogLevel <= LogLevel.WARNING:
        printer.print_yellow(format_message(*args))


def error(*args):
    if CurrentLogLevel <= LogLevel.ERROR:
        printer.print_red(format_message(*args))


def info(*args):
    if CurrentLogLevel <= LogLevel.INFO:
        printer.print_default(format_message(*args))


def debug(*args):
    if CurrentLogLevel <= LogLevel.DEBUG:
        printer.print_default(format_message(*args))


def critical(*args):
    if CurrentLogLevel <= LogLevel.CRITICAL:
        printer.print_red(format_message(*args))
