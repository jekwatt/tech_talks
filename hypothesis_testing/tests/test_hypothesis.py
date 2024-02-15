import pytest

from hypothesis import given, strategies as st
from hypothesis.strategies import lists, integers, floats, text


@given(lists(elements=integers()) | lists(elements=floats()) | lists(elements=text()))
def test_sorted_property_based(arg):
    result = sorted(arg)
    assert result == sorted(result)

