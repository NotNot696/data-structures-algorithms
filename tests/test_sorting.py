"""
Tests for Sorting Algorithms
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort


def test_sorting():
    arr = [5, 2, 8, 1, 3]
    expected = [1, 2, 3, 5, 8]

    assert bubble_sort(arr[:]) == expected
    assert selection_sort(arr[:]) == expected
    assert insertion_sort(arr[:]) == expected
    assert merge_sort(arr[:]) == expected
    assert quick_sort(arr[:]) == expected

    print(" All sorting tests passed!")


if __name__ == "__main__":
    test_sorting()