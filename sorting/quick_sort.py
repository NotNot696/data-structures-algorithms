"""
Quick Sort Algorithm
"""

import random


def quick_sort(arr):
    """
    Sort array using quick sort.

    Parameters:
        arr (list): Array to sort.

    Returns:
        list: Sorted array.

    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def main():
    arr = [5, 2, 8, 1, 3]
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()