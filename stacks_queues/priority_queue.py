"""
Priority Queue using List (Sorted Insertion)
"""


class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def enqueue(self, item):
        self.elements.append(None)
        i = self.length - 1

        while i >= 0 and self.elements[i] > item:
            self.elements[i + 1] = self.elements[i]
            i -= 1

        self.elements[i + 1] = item
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")

        item = self.elements[0]

        for i in range(self.length - 1):
            self.elements[i] = self.elements[i + 1]

        self.length -= 1
        self.elements.pop()
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0]

    def __str__(self):
        if self.is_empty():
            return "Priority Queue is empty"
        return "Priority Queue: " + " -> ".join(str(self.elements[i]) for i in range(self.length))


def main():
    pq = PriorityQueue()
    pq.enqueue(30)
    pq.enqueue(10)
    pq.enqueue(20)
    pq.enqueue(5)

    print(pq)
    print("Dequeue:", pq.dequeue())
    print(pq)


if __name__ == "__main__":
    main()