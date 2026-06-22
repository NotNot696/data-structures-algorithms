"""
Circular Queue Data Structure
"""


class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.array = [None] * size
        self.front = 0
        self.rear = -1
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("enqueue to full queue")

        self.rear = (self.rear + 1) % self.size
        self.array[self.rear] = item
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self.array[self.front]
        self.front = (self.front + 1) % self.size
        self.length -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.front]

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"

        result = []
        index = self.front
        for _ in range(self.length):
            result.append(str(self.array[index]))
            index = (index + 1) % self.size
        return "Queue: " + " -> ".join(result)


def main():
    q = CircularQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)

    q.dequeue()
    q.enqueue(40)
    print(q)


if __name__ == "__main__":
    main()