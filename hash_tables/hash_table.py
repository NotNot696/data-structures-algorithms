"""
Hash Table with Chaining
"""


class HashTable:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.length = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        new_entry = self.Entry(key, value)

        if self.table[index] is None:
            self.table[index] = [new_entry]
            self.length += 1
        else:
            found = False
            for i, e in enumerate(self.table[index]):
                if e.key == key:
                    self.table[index][i] = new_entry
                    found = True
                    break
            if not found:
                self.table[index].append(new_entry)
                self.length += 1

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for e in self.table[index]:
            if e.key == key:
                return e.value
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for i, e in enumerate(self.table[index]):
            if e.key == key:
                deleted = e.value
                del self.table[index][i]
                self.length -= 1
                return deleted
        return None

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket is None:
                result.append(f"{i}: []")
            else:
                items = " -> ".join([f"{e.key}: {e.value}" for e in bucket])
                result.append(f"{i}: [{items}]")
        return "\n".join(result)


def main():
    ht = HashTable(5)
    ht.insert("apple", "سیب")
    ht.insert("banana", "موز")
    ht.insert("grape", "انگور")
    ht.insert("apple", "آپل")

    print(ht)
    print("Get apple:", ht.get("apple"))
    print("Remove banana:", ht.remove("banana"))
    print(ht)


if __name__ == "__main__":
    main()