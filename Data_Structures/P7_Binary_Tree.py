#Write a program to implement Binary Tree with insertion, deletion, traversal operations
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    def _delete_recursive(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            min_node = self._find_min(current.right)
            current.key = min_node.key
            current.right = self._delete_recursive(current.right, min_node.key)
        return current
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)
    def preorder_traversal(self, node):
        if node is not None:
            print(node.key, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")
# Example Usage:
tree = BinaryTree()
# Insertion
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
# Traversal
print("Inorder Traversal:")
tree.inorder_traversal(tree.root)
# Output: 20 30 40 50 60 70 80
# Deletion
tree.delete(30)
# Traversal after deletion
print("\nInorder Traversal after deletion:")
tree.inorder_traversal(tree.root)
# Output: 20 40 50 60 70 80

