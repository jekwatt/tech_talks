from collections import Counter

import pytest


def test_sorted_manually_ints():
    assert sorted([1, 2, 3]) == [1, 2, 3]


def test_sorted_manually_floats():
    assert sorted([3.0, 2.0, 1.0]) == [1.0, 2.0, 3.0]


def test_sorted_manually_strings():
    assert sorted(["b", "c", "a"]) == ["a", "b", "c"]
