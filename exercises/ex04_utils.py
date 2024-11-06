"""Not sure what this is"""

__author__ = "730751255"


def all(list: list[int], int: int) -> bool:
    is_true: bool = True
    if list == []:
        is_true = False
        # need this so that an empty list is returned as false
    for elem in list:
        if elem != int:
            is_true = False
    return is_true


def max(vals: list[int]) -> int:
    if len(vals) == 0:
        raise ValueError("max() arg is an empty List")
    biggest_int: int = vals[0]
    # have to start with index 0 being out of the loop so that there isn't-
    # an error with the bounds (can't have index of -1)
    for i in range(1, len(vals)):
        if vals[i] > vals[i - 1]:
            biggest_int = vals[i]
    return biggest_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    equal: bool = True
    if len(list1) != len(list2):
        equal = False
    for i in range(0, len(list1)):
        # better to use i in range loop rather than for elem loop so that-
        # I don't need nested loop
        if list1[i] != list2[i]:
            equal = False
    return equal


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:
        list1.append(elem)
