import re


def parse_line(line: str):
    """Parse a line of the form ``key=value`` and return a dictionary.

    The original implementation used the walrus operator (``:=``) which
    requires Python 3.8+.  The CI environment runs Python 3.7, so we
    rewrite the logic to be compatible while keeping the behaviour
    identical.
    """
    m = re.match(r"(\w+)=(\d+)", line)
    if m:
        key, value = m.group(1), int(m.group(2))
        return {key: value}
    return None
