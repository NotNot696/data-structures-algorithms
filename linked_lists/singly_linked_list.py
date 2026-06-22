"""
Singly Linked List Implementation
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        if index == self.length:
            self.append(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError("delete from empty list")

        deleted = self.head.data
        self.head = self.head.next
        self.length -= 1
        return deleted

    def delete_last(self):
        if self.is_empty():
            raise IndexError("delete from empty list")

        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            self.length -= 1
            return deleted

        current = self.head
        while current.next.next:
            current = current.next

        deleted = current.next.data
        current.next = None
        self.length -= 1
        return deleted

    def delete_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            return self.delete_first()

        if index == self.length - 1:
            return self.delete_last()

        current = self.head
        for _ in range(index - 1):
            current = current.next

        deleted = current.next.data
        current.next = current.next.next
        self.length -= 1
        return deleted

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"


def main():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("List:", ll.display())

    ll.prepend(5)
    print("After prepend:", ll.display())

    ll.insert_at(2, 15)
    print("After insert at index 2:", ll.display())

    ll.delete_first()
    print("After delete first:", ll.display())

    ll.delete_last()
    print("After delete last:", ll.display())


if __name__ == "__main__":
    main()