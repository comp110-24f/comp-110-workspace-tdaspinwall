__author__ = "730751255"


def find_and_remove_max(vals: list[int]) -> int:
    if vals == []:
        return -1
    biggest_val: int = vals[0]
    for elem in vals:
        if elem > biggest_val:
            biggest_val = elem
    index: int = 0
    while index < len(vals):
        if vals[index] == biggest_val:
            vals.pop(index)
        else:
            index += 1
    return biggest_val
