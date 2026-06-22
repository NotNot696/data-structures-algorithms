"""
Insertion Sort Algorithm
"""


def insertion_sort(arr):
    """
    Sort array using insertion sort.

    Parameters:
        arr (list): Array to sort.

    Returns:
        list: Sorted array.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def main():
    arr = [5, 2, 8, 1, 3]
    sorted_arr = insertion_sort(arr)
    print(f"Sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()