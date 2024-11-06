"""Mutating functions."""

__author__ = "730751255"


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], int: int) -> None:
    a.append(int)


def double(a: list[int]) -> None:
    index: int = 0
    while index < len(a):
        a[index] = a[index] * 2
        index += 1


double(list_2)
print(list_1)
print(list_2)
