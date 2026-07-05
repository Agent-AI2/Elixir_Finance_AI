import re

DATE_PATTERN = r"^\d{2}-[A-Z]{3}-\d{2}$"


def is_transaction(row):

    if row is None:
        return False

    if len(row) < 6:
        return False

    if row[0] is None:
        return False

    return bool(re.match(DATE_PATTERN, str(row[0]).strip()))