"""
Tests for Searching Algorithms
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from searching.linear_search import linear_search
from searching.binary_search import binary_search
from searching.ternary_search import ternary_search


def test_searching():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    assert linear_search(arr, 7) == 3
    assert linear_search(arr, 99) == -1

    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 99) == -1

    assert ternary_search(arr, 7) == 3
    assert ternary_search(arr, 99) == -1

    print("All searching tests passed!")


if __name__ == "__main__":
    test_searching()