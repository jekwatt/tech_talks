import pytest

from hypothesis import given, strategies as st
from hypothesis.strategies import lists, integers, floats, text


# Defines lists with different types of elements using hypothesis.strategies.lists
@given(lists(elements=integers()) | lists(elements=floats()) | lists(elements=text()))
def test_sorted_property_based_a(arg):
    result = sorted(arg)
    assert result == sorted(result)

