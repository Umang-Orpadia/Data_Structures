class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
    def is_empty(self):
        return len(self.items) == 0
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
    def traverse(self):
        print("Queue Contents:")
        for item in self.items:
            print(item, end=' ')
        print()
# Example Usage:
queue = Queue()
# Insertion (Enqueue)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
# Traversal
queue.traverse()
# Output: Queue Contents: 5 10 15
# Deletion (Dequeue)
dequeued_item = queue.dequeue()
print(f"Dequeued item: {dequeued_item}")
# Traversal after deletion
queue.traverse()
# Output: Queue Contents: 10 15
# Front (front element without dequeuing)
front_element = queue.front()
print(f"Front element: {front_element}")
# Output: Front element: 10
