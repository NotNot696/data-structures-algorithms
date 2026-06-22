"""
Ternary Search Algorithm
"""


def ternary_search(arr, target):
    """
    Ternary search in a sorted array.

    Parameters:
        arr (list): Sorted array.
        target: Value to find.

    Returns:
        int: Index of target if found, otherwise -1.

    Time Complexity: O(log₃ n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = ternary_search(arr, target)
    print(f"Index of {target}: {result}")


if __name__ == "__main__":
    main()