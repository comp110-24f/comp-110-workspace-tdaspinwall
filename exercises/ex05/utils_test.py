from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


"""tests for ex05"""

__author__ = "730751255"


# tests that the return value is functioning
def test_only_evens_return() -> None:
    vals: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(vals) == [2, 4, 6, 8, 10]


# tests that the list is not mutated
def test_only_evens_mutate() -> None:
    vals: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    only_evens(vals)
    assert vals == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# tests that using an empty list doesn't cause problems
def test_only_evens_edge_empty_list() -> None:
    vals: list[int] = []
    assert only_evens(vals) == []


def test_sub_return() -> None:
    vals: list[int] = [10, 20, 30, 40]
    assert sub(vals, 1, 3) == [20, 30]


def test_sub_mutate() -> None:
    vals: list[int] = [10, 20, 30, 40]
    sub(vals, 1, 3)
    assert vals == [10, 20, 30, 40]


def test_sub_edge_weird_bounds() -> None:
    vals: list[int] = [10, 20, 30, 40]
    assert sub(vals, -1, 6) == [10, 20, 30, 40]


# add_at_index mutates the list instead of returning a list
def test_add_at_index_return() -> None:
    vals: list[int] = [4, 5, 6, 9]
    assert add_at_index(vals, 7, 3) is None
    # for some reason you say 'is' rather than '=='


def test_add_at_index_mutate() -> None:
    vals: list[int] = [4, 5, 6, 9]
    add_at_index(vals, 7, 3)
    assert vals == [4, 5, 6, 7, 9]


def test_add_at_index_index_error() -> None:
    vals: list[int] = [4, 5, 6, 9]
    with pytest.raises(IndexError):
        add_at_index(vals, 7, 10)
