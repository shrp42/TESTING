# < 7. Графы >
from collections import deque, defaultdict

# -------------------------
# Класс Graph
# -------------------------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)  # adjacency list

    def add_edge(self, u, v):
        self.adj[u].append(v)


# ----------------------------------------------------------------------


# -------------------------
# BFS Traversal (from source)
# -------------------------
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

# -------------------------
# DFS Traversal (recursive)
# -------------------------
    def dfs_util(self, node, visited, result):
        visited[node] = True
        result.append(node)
        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, result)

    def dfs(self, start):
        visited = [False] * self.V
        result = []
        self.dfs_util(start, visited, result)
        return result


# ----------------------------------------------------------------------


# -------------------------
# Cycle Detection in Directed Graph (DFS)
# -------------------------
    def is_cyclic_util(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.adj[node]:
            if not visited[neighbor] and self.is_cyclic_util(neighbor, visited, rec_stack):
                return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


# ----------------------------------------------------------------------


# -------------------------
# Shortest Path in Unweighted Graph (BFS)
# -------------------------
    def shortest_path_unweighted(self, start):
        dist = [float('inf')] * self.V
        dist[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if dist[neighbor] == float('inf'):
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        return dist


# ----------------------------------------------------------------------


# -------------------------
# Topological Sorting (DFS)
# -------------------------
    def topological_sort_util(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(node)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for node in range(self.V):
            if not visited[node]:
                self.topological_sort_util(node, visited, stack)
        return stack[::-1]  # reverse stack for correct order


# ----------------------------------------------------------------------


# -------------------------
# Пример использования
# -------------------------
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("BFS from node 5 :", g.bfs(5))
    print("DFS from node 5 :", g.dfs(5))
    print("Graph has cycle  :", g.is_cyclic())
    print("Shortest paths from node 5 :", g.shortest_path_unweighted(5))
    print("Topological sort :", g.topological_sort())
