import pytest

from hypothesis import given, strategies as st
from hypothesis.strategies import lists, integers, floats, text


# Defines lists with different types of elements using hypothesis.strategies.lists
@given(lists(elements=integers()) | lists(elements=floats()) | lists(elements=text()))
def test_sorted_property_based_a(arg):
    result = sorted(arg)
    assert result == sorted(result)


# Uses the given decorator along with Hypothesis strategies directly
@given(st.lists(st.integers() | st.floats() | st.text()))
def test_sorted_property_based_b(input_list):
    # Cast all elements to strings before sorting
    input_list = [str(element) for element in input_list]
    result = sorted(input_list)
    assert result == sorted(result)
