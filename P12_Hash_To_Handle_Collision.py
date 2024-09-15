class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)
    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        if current is None:
            print(f"Key {key} not found")
            return
        if current.key == key:
            self.table[index] = current.next
            return
        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        print(f"Key {key} not found")
    def traverse(self):
        print("Hash Table Contents:")
        for i in range(self.size):
            current = self.table[i]
            while current is not None:
                print(f"Key: {current.key}, Value: {current.value}")
                current = current.next
        print()
# Example Usage:
hash_table = HashTable(10)
# Insertion
hash_table.insert(5, 'apple')
hash_table.insert(2, 'banana')
hash_table.insert(7, 'cherry')
hash_table.insert(12, 'date')  # Collides with 2
# Traversal
hash_table.traverse()
# Output:
# Hash Table Contents:
# Key: 2, Value: banana
# Key: 12, Value: date
# Key: 5, Value: apple
# Key: 7, Value: cherry
# Retrieval
print("Value for key 5:", hash_table.get(5))  # Output: Value for key 5: apple
# Deletion
hash_table.delete(2)
# Traversal after deletion
hash_table.traverse()
# Output:
# Hash Table Contents:
# Key: 12, Value: date
# Key: 5, Value: apple
# Key: 7, Value: cherry




