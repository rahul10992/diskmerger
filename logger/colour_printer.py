def print_coloured(text: str, color_code: str) -> None:
    print(f"\033[{color_code}m{text}\033[0m")


def print_red(text: str) -> None:
    print_coloured(text, "31")


def print_yellow(text: str) -> None:
    print_coloured(text, "33")


def print_green(text: str) -> None:
    print_coloured(text, "32")


def print_default(text: str) -> None:
    print(text)
