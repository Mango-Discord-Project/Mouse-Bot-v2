def ascii_check(string: str) -> list:
    ascii_range = range(32, 127)
    return [(index, char) for index, char in enumerate(string) if ord(char) not in ascii_range]