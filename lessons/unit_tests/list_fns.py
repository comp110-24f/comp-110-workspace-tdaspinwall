def get_first(vals: list[str]) -> str:
    return vals[0]


def remove_first(vals: list[str]) -> None:
    vals.pop(0)


def get_and_remove_first(vals: list[str]) -> str:
    first_item: str = vals[0]
    vals.pop(0)
    return first_item
