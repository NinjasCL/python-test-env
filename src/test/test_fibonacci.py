import pytest
from .. import fibonacci as fib


def test_that_recursive_works():
    result = fib.recursive(5)
    assert result == 5


def test_that_memoization_works():
    result = fib.memoization(50)
    assert result == 12586269025


def test_that_iterative_works():
    result = fib.iterative(5)
    assert result == 5

    result = fib.iterative(50)
    assert result == 12586269025
