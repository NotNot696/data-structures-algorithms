"""
Dynamic Array Implementation
"""


class DynamicArray:
    def __init__(self, size=5):
        self.size = size
        self.array = [None] * size
        self.length = 0

    def _resize(self):
        self.size *= 2
        new_array = [None] * self.size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def is_empty(self):
        return self.length == 0

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if self.length == self.size:
            self._resize()

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.length - 1] = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        self.array[index] = value

    def append(self, value):
        self.insert(self.length, value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty array")
        value = self.get(self.length - 1)
        self.remove(self.length - 1)
        return value

    def __str__(self):
        return str(self.array[:self.length])


def main():
    arr = DynamicArray(3)
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print("Array:", arr)

    arr.insert(1, 15)
    print("After insert:", arr)

    arr.remove(2)
    print("After remove:", arr)


if __name__ == "__main__":
    main()