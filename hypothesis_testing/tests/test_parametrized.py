from collections import Counter

import pytest


SORTED_TEST_CASES = [
    ([1, 2, 3], [1, 2, 3]),
    ([3.0, 2.0, 1.0], [1.0, 2.0, 3.0]),
    (["b", "c", "a"], ["a", "b", "c"]),
]

@pytest.mark.parametrize(
    "arg, result",
    SORTED_TEST_CASES,
)
def test_sorted_parametrized_with_known_results(arg, result):
    assert sorted(arg) == result
