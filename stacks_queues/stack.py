"""
Stack Data Structure (LIFO)
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack:", s)
    print("Pop:", s.pop())
    print("Peek:", s.peek())
    print("Size:", s.size())


if __name__ == "__main__":
    main()