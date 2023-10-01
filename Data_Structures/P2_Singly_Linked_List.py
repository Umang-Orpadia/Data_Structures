class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def delete(self, data):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None and temp.next.data != data:
            temp = temp.next
        if temp.next is None:
            print(f"{data} not found in the list")
        else:
            temp.next = temp.next.next
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
# Example Usage:
linked_list = LinkedList()
# Insertion
linked_list.insert(5)
linked_list.insert(10)
linked_list.insert(15)
# Traversal
print("Linked List:")
linked_list.traverse()
# Output: Linked List: 5 10 15
# Deletion
linked_list.delete(10)
# Traversal after deletion
print("Linked List after deletion:")
linked_list.traverse()
# Output: Linked List after deletion: 5 15
