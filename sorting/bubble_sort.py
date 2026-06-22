"""
Bubble Sort Algorithm
"""


def bubble_sort(arr):
    """
    Sort array using bubble sort.

    Parameters:
        arr (list): Array to sort.

    Returns:
        list: Sorted array.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def main():
    arr = [5, 2, 8, 1, 3]
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()