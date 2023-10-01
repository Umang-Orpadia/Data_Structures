class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = (key, value)
    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None
        else:
            print(f"Key {key} not found")
    def traverse(self):
        print("Hash Table Contents:")
        for entry in self.table:
            if entry:
                print(f"Key: {entry[0]}, Value: {entry[1]}")
        print()
# Example Usage:
hash_table = HashTable(10)
# Insertion
hash_table.insert(5, 'apple')
hash_table.insert(2, 'banana')
hash_table.insert(7, 'cherry')
# Traversal
hash_table.traverse()
# Output:
# Hash Table Contents:
# Key: 5, Value: apple
# Key: 2, Value: banana
# Key: 7, Value: cherry
# Deletion
hash_table.delete(2)
# Traversal after deletion
hash_table.traverse()
# Output:
# Hash Table Contents:
# Key: 5, Value: apple
# Key: 7, Value: cherry

