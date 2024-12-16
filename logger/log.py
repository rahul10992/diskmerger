import print_colour as printer


def Warning(txt):
    printer.print_yellow(txt)


def Error(str):
    printer.print_red(str)


def Info(str):
    printer.print_default(str)


def Debug(str):
    printer.print_default(str)


def Critical(str):
    printer.print_red("CRITICAL: " + str)
