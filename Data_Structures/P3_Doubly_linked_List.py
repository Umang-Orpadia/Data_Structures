class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
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
            new_node.prev = temp
    def delete(self, data):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        temp = self.head
        while temp is not None and temp.data != data:
            temp = temp.next
        if temp is None:
            print(f"{data} not found in the list")
        else:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
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
linked_list = DoublyLinkedList()
# Insertion
linked_list.insert(5)
linked_list.insert(10)
linked_list.insert(15)
# Traversal
print("Doubly Linked List:")
linked_list.traverse()
# Output: Doubly Linked List: 5 10 15
# Deletion
linked_list.delete(10)
# Traversal after deletion
print("Doubly Linked List after deletion:")
linked_list.traverse()
# Output: Doubly Linked List after deletion: 5 15
