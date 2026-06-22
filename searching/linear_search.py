"""
Linear Search Algorithm
"""


def linear_search(arr, target):
    """
    Linear search in an array.

    Parameters:
        arr (list): The array to search in.
        target: The value to find.

    Returns:
        int: Index of the target if found, otherwise -1.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    arr = [3, 7, 1, 9, 5]
    target = 9
    result = linear_search(arr, target)
    print(f"Index of {target}: {result}")


if __name__ == "__main__":
    main()