import pytest
from arith import multiply,add

def test_add_with_correct_values():
    assert(add(2,3) == 5)

def test_multiply_with_correct_values():
    assert(multiply(3,6) == 18)

