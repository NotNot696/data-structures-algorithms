"""
Max Heap Implementation
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] > self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left

            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            raise IndexError("remove from empty heap")

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


def main():
    heap = MaxHeap()
    for v in [10, 20, 5, 30, 15]:
        heap.insert(v)

    print("Heap:", heap)
    print("Remove:", heap.remove())
    print("After remove:", heap)


if __name__ == "__main__":
    main()