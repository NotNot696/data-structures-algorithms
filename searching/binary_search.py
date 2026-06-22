"""
Binary Search Algorithm
"""


def binary_search(arr, target):
    """
    Binary search in a sorted array.

    Parameters:
        arr (list): Sorted array.
        target: Value to find.

    Returns:
        int: Index of target if found, otherwise -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(arr, target)
    print(f"Index of {target}: {result}")


if __name__ == "__main__":
    main()