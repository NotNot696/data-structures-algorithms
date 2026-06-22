"""
Helper Functions
"""


def print_array(arr):
    print(" ".join(str(x) for x in arr))


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def print_graph(adj_list):
    for v, neighbors in adj_list.items():
        print(f"{v}: {neighbors}")