class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
    def traverse(self):
        print("Stack Contents:")
        for item in self.items:
            print(item, end=' ')
        print()
# Example Usage:
stack = Stack()
# Insertion (Push)
stack.push(5)
stack.push(10)
stack.push(15)
# Traversal
stack.traverse()
# Output: Stack Contents: 5 10 15
# Deletion (Pop)
popped_item = stack.pop()
print(f"Popped item: {popped_item}")
# Traversal after deletion
stack.traverse()
# Output: Stack Contents: 5 10
# Peek (top element without popping)
top_element = stack.peek()
print(f"Top element: {top_element}")
# Output: Top element: 10

