"""ex05"""

__author__ = "730751255"


def only_evens(vals: list[int]) -> list[int]:
    new_vals: list[int] = []
    for elem in vals:
        if (elem % 2) == 0:
            new_vals.append(elem)
    return new_vals


def sub(vals: list[int], start_index: int, end_index: int) -> list[int]:
    new_vals: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(vals):
        end_index = len(vals)
    for i in range(start_index, end_index):
        new_vals.append(vals[i])
    return new_vals


def add_at_index(vals: list[int], int_elem: int, index: int) -> None:
    if index > len(vals) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    vals.append(0)
    # add a integer at the end of the list
    for i in range(len(vals) - 1, index, -1):
        vals[i] = vals[i - 1]
    vals[index] = int_elem
    """shifts everything over"""
