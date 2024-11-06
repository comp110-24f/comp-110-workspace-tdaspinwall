"""Summing the elements of a list using different loops"""

__author__ = "730751255"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum
