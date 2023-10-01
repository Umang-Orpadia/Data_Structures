import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def enqueue(self, element, priority):
        heapq.heappush(self.elements, (priority, element))
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]
        else:
            print("Priority Queue is empty")
    def is_empty(self):
        return len(self.elements) == 0
    def traverse(self):
        print("Priority Queue Contents:")
        for _, element in self.elements:
            print(element, end=' ')
        print()
# Example Usage:
priority_queue = PriorityQueue()
# Insertion (Enqueue)
priority_queue.enqueue("Task A", 3)
priority_queue.enqueue("Task B", 1)
priority_queue.enqueue("Task C", 2)
# Traversal
priority_queue.traverse()
# Output: Priority Queue Contents: Task B Task C Task A
# Deletion (Dequeue)
dequeued_task = priority_queue.dequeue()
print(f"Dequeued task: {dequeued_task}")

# Traversal after deletion
priority_queue.traverse()
# Output: Priority Queue Contents: Task C Task A
