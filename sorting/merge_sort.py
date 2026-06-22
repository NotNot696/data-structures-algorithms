
"""
Merge Sort Algorithm
"""


def merge_sort(arr):
    """
    Sort array using merge sort.

    Parameters:
        arr (list): Array to sort.

    Returns:
        list: Sorted array.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    arr = [5, 2, 8, 1, 3]
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()