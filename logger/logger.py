from . import colour_printer as printer


def format_message(*args) -> str:
    return " ".join(map(str, args))


def warning(*args):
    printer.print_yellow(format_message(*args))


def error(*args):
    printer.print_red(format_message(*args))


def info(*args):
    printer.print_default(format_message(*args))


def debug(*args):
    printer.print_default(format_message(*args))


def critical(*args):
    printer.print_red(format_message(*args))
