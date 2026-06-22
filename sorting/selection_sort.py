"""
Selection Sort Algorithm
"""


def selection_sort(arr):
    """
    Sort array using selection sort.

    Parameters:
        arr (list): Array to sort.

    Returns:
        list: Sorted array.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    arr = [5, 2, 8, 1, 3]
    sorted_arr = selection_sort(arr)
    print(f"Sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()