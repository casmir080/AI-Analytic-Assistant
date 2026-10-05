import re


def is_safe_query(query: str) -> bool:
    query = query.strip().lower()

    # Must start with SELECT
    if not query.startswith("select"):
        return False

    # Block dangerous keywords
    forbidden = ["insert", "update", "delete", "drop", "alter", "truncate"]

    for word in forbidden:
        if re.search(rf"\b{word}\b", query):
            return False

    return True