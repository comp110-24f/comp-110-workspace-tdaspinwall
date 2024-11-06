__author__ = "730751255"

from CQs.cq07.find_max import find_and_remove_max


def test_return_find_and_remove_max() -> None:
    vals: list[int] = [1, 3, 5, 11, 5, 11]
    assert find_and_remove_max(vals) == 11


def test_mutate_find_and_remove_max() -> None:
    vals: list[int] = [1, 3, 5, 11, 5, 11]
    find_and_remove_max(vals)
    assert vals == [1, 3, 5, 5]


def test_edge_find_and_remove_max() -> None:
    vals: list[int] = []
    assert find_and_remove_max(vals) == -1
