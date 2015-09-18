import re


def get_prefix_suffix(version, line):
    """
    If the version is in the given line, return the prefix and suffix, else None, None.
    """
    match = re.match(r"(.*)%s(.*)" % re.escape(version), line)
    if match is None:
        return None, None
    return match.groups()


def get_version_lines(version, lines):
    """
    Finds all occurences of the version number in the given list of strings and return the
    prefixes and suffixes as a dictionary of tuples with the (1 based) line numbers as keys.
    """
    ret = {}
    for i, line in enumerate(lines, 1):
        pre_suf = get_prefix_suffix(version, line)
        if not any([x is None for x in pre_suf]):
            ret[i] = pre_suf
    return ret
