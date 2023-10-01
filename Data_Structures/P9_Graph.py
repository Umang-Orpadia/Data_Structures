class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        else:
            print(f"Edge ({u}, {v}) does not exist")
    def dfs(self, start):
        visited = set()
        def dfs_util(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_util(neighbor)
        dfs_util(start)
        print()
    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()
# Example Usage:
g = Graph()
# Insertion (Adding edges)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
# Traversal (DFS)
print("Depth First Search:")
g.dfs(1)
# Output: 1 2 3 4
# Traversal (BFS)
print("Breadth First Search:")
g.bfs(1)
# Output: 1 2 3 4
# Deletion (Removing edge)
g.remove_edge(2, 3)
# Traversal after deletion (DFS)
print("Depth First Search after deletion:")
g.dfs(1)
# Output: 1 3 4
# Traversal after deletion (BFS)
print("Breadth First Search after deletion:")
g.bfs(1)
# Output: 1 3 4
