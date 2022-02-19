import re

def parse_input(s: list):
    if len(s) == 1:
        return int(s[0]) if bool(re.match("^([1-9][0-9]{4})$", s[0])) else -1
    return -1
