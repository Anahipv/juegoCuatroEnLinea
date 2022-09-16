import pytest
from list_utils import *

def test_find_one():
    needle = 1
    none = [0, 0, 5, 's']
    beginning = [1, None, 9, 6, 0, 0]
    end = ['x', 'o', 1]
    several = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(end, needle)
    assert find_one(several, needle)

def test_find_n():
    assert find_n([2, 3, 4, 5, 6], 2, -1) == False
    assert find_n([2, 3, 4, 5, 6], 42, 2) == False
    assert find_n([2, 3, 1, 5, 6], 1, 2) == False
    assert find_n([2, 3, 4, 5, 6, 3, 2], 2, 2)
    assert find_n([2, 3, 4, 5, 6, 4, 6, 3, 4, 4, 6, 7], 4, 2)
    assert find_n([1, 2, 3, 4], 'x', 0) == True
    assert find_n([2, 3, 4, 5, 6], 42, 1) == False

def test_find_streak():
    assert find_streak([2, 3, 4, 5, 6], 4, -1) == False
    assert find_streak([2, 3, 4, 5, 6], 42, 2) == False
    assert find_streak([2, 3, 4, 5, 6], 4, 1)
    assert find_streak([2, 3, 4, 5, 6, 3, 2], 2, 2) == False
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 3)
    assert find_streak([5, 5, 5, 1, 2, 3, 4], 5, 3)
    assert find_streak([2, 3, 4, 5, 5, 5, 6, 1], 5, 3)
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 4) == False