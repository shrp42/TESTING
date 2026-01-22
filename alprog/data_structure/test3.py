# LESSON 5/6:
from collections import *
from idlelib.debugger_r import restart_subprocess_debugger
from inspect import stack
from pydoc import visiblename


# class TreeNode:
#     def __init__(self, val = 0, right = None, left = None):
#         self.val = val
#         self.right = right
#         self.left = left
#
#
# class BinaryTree:
#     def __init__(self, root = None):
#         self.root = root
#
#
# def inorder(self, node):
#     if not node:
#         return []
#     return self.inorder(node.left) + [node.val] + self.inorder(node.right)
#
# def preorder(self, node):
#     if not node:
#         return []
#     return [node.val] + self.preorder(node.left) + self.preorder(node.right)
#
# def postorder(self, node):
#     if not node:
#         return []
#     return self.postorder(node.left) + self.postorder(node.right) + [node.val]
#
#
# def max_depth(self, node):
#     if not node:
#         return []
#     return 1 + max(self.max_depth(node.left), self.max_depth(node.right))
#
#
# def lowest_common_ancestor(self, node, p, q):
#     if not node or node == p or node == q:
#         return node
#
#     left = self.lowest_common_ancestor(node.left, p , q)
#     right = self.lowest_common_ancestor(node.right, p, q)
#
#     if right and left:
#         return node
#     return left or right
#
#
# def serialize(self, node):
#     if not node:
#         return ""
#
#     result = []
#     queue = deque([node])
#
#     while queue:
#         n = queue.popleft()
#         if n:
#             result.append(str(n.val))
#             queue.append(n.left)
#             queue.append(n.right)
#         else:
#             result.append("#")
#     return ",".join(result)
#
#
# def deserialize(self, data):
#     if not data:
#         return None
#
#     vals = data.split(",")
#     root = TreeNode(int(val[0]))
#     queue = deque([root])
#     i = 1
#
#     while queue and i < len(vals):
#         node = queue.popleft()
#         if vals[i] != "#":
#             node.left = TreeNode(int(val[i]))
#             queue.append(node.left)
#         i += 1
#
#         if i < len[vals] and vals[i] != "#":
#             node.right = TreeNode(int(val[i]))
#             queue.append(node.right)
#         i += 1
#
#     return root




# class TreeNode:
#     def __init__(self, val = 0, right = None, left = None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class BinaryTree:
#     def __init__(self, root = None):
#         self.root = root
#
# def inorder(self, node):
#     if not node:
#         return []
#     return self.inorder(node.left) + [node.val] + self.inorder(node.right)
#
# def preorder(self, node):
#     if not node:
#         return []
#     return [node.val] + self.preorder(node.left) + self.preorder(node.right)
#
# def postorder(self, node):
#     if not node:
#         return []
#     return self.postorder(node.left) + self.postorder(node.right) + [node.val]
#
#
# def max_depth(self, node):
#     if not node:
#         return 0
#     return 1 + max(self.max_depth(node.left), self.max_depth(node.right))
#
#
# def lowest_common_ancestor(self, node, p, q):
#     if not node or node == p or node == q:
#         return node
#
#     left = self.lowest_common_ancestor(node.left, p, q)
#     right = self.lowest_common_ancestor(node.right, p, q)
#
#     if left and right:
#          return node
#     return left or right
#
#
# def serialize(self, node):
#     if not node:
#         return ""
#
#     result = []
#     queue = deque([node])
#
#     while queue:
#         n = queue.popleft()
#         if n:
#             result.append(str(n.val))
#             queue.append(n.left)
#             queue.append(n.right)
#         else:
#             result.append("#")
#
#     return ",".join(result)
#
#
# def deserialize(self, data):
#     if not data:
#         return None
#
#     vals = data.split(",")
#     root = TreeNode(int(vals[0]))
#     queue = deque([root])
#     i = 1
#
#     while queue and i < len(vals):
#         node = queue.popleft()
#
#         if vals[i] != "#":
#             node.left = TreeNode(int(vals[i]))
#             queue.append(node.left)
#         i += 1
#
#         if i < len(vals) and vals[i] != "#":
#             node.right = TreeNode(int(vals[i]))
#             queue.append(node.right)
#         i += 1
#
#     return root


class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self, root):
        self.root = root



    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def preorder(self, node):
        if not node:
            return []
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.val]



    def max_depth(self, node):
        if not node:
            return 0

        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))



    def lowest_common_ancestor(self, node, p, q):
        if not node or node == p or node == q:
            return node

        left = self.lowest_common_ancestor(node.left, p, q)
        right = self.lowest_common_ancestor(node.right, p, q)

        if left and right:
            return node
        return left or right



    def serialize(self, node):
        if not node:
            return ""

        result = []
        queue = deque([node])

        while queue:
            n = queue.popleft()
            if n:
                result.append(str(n.val))
                queue.append(n.left)
                queue.append(n.right)
            else:
                result.append("#")

        return ",".join(result)



    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(vals):
            node = queue.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root

# root = TreeNode(1,
#         TreeNode(2),
#         TreeNode(3, TreeNode(4), TreeNode(5))
# )
#
# tree = BinaryTree(root)
#
# print(tree.inorder(tree.root))      # [2, 1, 4, 3, 5]
# print(tree.max_depth(tree.root))    # 3
#
# data = tree.serialize(tree.root)
# print(data)
#
# new_root = tree.deserialize(data)
# print(tree.preorder(new_root))



def two_sum(nums: list(int), target: int) -> list[int]:

    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

    if diff in seen:
        return [seen[diff, i]]

    seen[num] = i


# LESSON 7

# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.adj = defaultdict(list)
#
#     def add_edge(self, u, v):
#         self.adj[u].append(v)
#
#
#     def bfs(self, start):
#
#         visited = [False] * self.V
#         queue = deque([start])
#         visited[start] = True
#         result = []
#
#         while queue:
#             node = queue.popleft()
#             result.append(node)
#
#             for neighbor in self.adj[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     queue.append(neighbor)
#
#         return result
#
#
#
#     def dfs_util(self, node, visited, result):
#         visited[node] = True
#         result.append(node)
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.dfs_util(neighbor, visited, result)
#
#     def dfs(self, start):
#         visited = [False] * self.V
#         result = []
#         self.dfs_util(start, visited, result)
#         return result
#
#
#
#     def cyclic_util(self, node, visited, rec_stack):
#         visited[node] = True
#         rec_stack[node] = True
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor] and self.cyclic_util(neighbor, visited, rec_stack):
#                 return True
#             elif rec_stack[neighbor]:
#                 return True
#
#         rec_stack[node] = False
#         return False
#
#     def cyclic(self):
#         visited = [False] * self.V
#         rec_stack = [False] * self.V
#
#         for node in range(self.V):
#             if not visited[node]:
#                 if self.cyclic_util(node, visited, rec_stack):
#                     return True
#
#         return False
#
#
#
#     def shortest_path(self, start):
#         dist = [float("inf")] * self.V
#         queue = deque([start])
#         dist[start] = 0
#
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.adj[node]:
#                 if dist[neighbor] == float("inf"):
#                     dist[neighbor] = dist[node] + 1
#                     queue.append(neighbor)
#
#         return dist
#
#
#
#     def topological_sorting_util(self, node, visited, stack):
#         visited[node] = True
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.topological_sorting_util(neighbor, visited, stack)
#         stack.append(node)
#
#     def topological_sort(self):
#         visited = [False] * self.V
#         stack = []
#
#         for node in range(self.V):
#             if not visited[node]:
#                 self.topological_sorting_util(node, visited, stack)
#         return stack[::-1]
#



# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.adj = defaultdict(list)
#
#     def add_edge(self, u, v):
#         self.adj[u].append(v)
#
#
#
#     def bfs(self, start):
#         visited = [False] * self.V
#         queue = deque([start])
#         visited[start] = True
#         result = []
#
#         while queue:
#             node = queue.popleft()
#             result.append(node)
#
#             for neighbor in self.adj[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     queue.append(neighbor)
#
#         return result
#
#
#
#     def dfs_util(self, node, visited, result):
#         visited[node] = True
#         result.append(node)
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.dfs_util(neighbor, visited, result)
#
#     def dfs(self, start):
#         visited = [False] * self.V
#         result = []
#         self.dfs_util(start, visited, result)
#         return result
#
#
#
#     def cyclic_util(self, node, visited, rec_stack):
#         visited[node] = True
#         rec_stack[node] = True
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor] and self.cyclic_util(neighbor, visited, rec_stack):
#                 return True
#             elif rec_stack[neighbor]:
#                 return True
#
#         rec_stack[node] = False
#         return False
#
#     def cyclic(self, start):
#         visited = [False] * self.V
#         rec_stack = [False] * self.V
#
#         for node in range(self.V):
#             if not visited[node]:
#                 if self.cyclic_util(node, visited, rec_stack):
#                     return True
#
#         return False
#
#
#
#     def shortest_path(self, start):
#         dist = [float("inf")] * self.V
#         dist[start] = 0
#         queue = deque([start])
#
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.adj[node]:
#                 if dist[neighbor] == float("inf"):
#                     dist[neighbor] = dist[node] + 1
#                     queue.append(neighbor)
#
#         return dist
#
#
#
#     def topological_sort_util(self, node, visited, stack):
#         visited[node] = True
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.topological_sort_util(neighbor, visited, stack)
#         stack.append(node)
#
#     def topological_sort(self, start):
#         visited = [False] * self.V
#         stack = []
#         for node in range(self.V):
#             if not visited[node]:
#                 self.topological_sort_util(node, visited, stack)
#         return stack[::-1]


# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.adj = defaultdict(list)
#
#     def add_edge(self, u, v):
#         self.adj[u].append(v)
#
#
#
#     def bfs(self, start):
#         visited = [False] * self.V
#         queue = deque([start])
#         visited[start] = True
#         result = []
#
#         while queue:
#             node = queue.popleft()
#             result.append(node)
#
#             for neighbor in self.adj[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     queue.append(neighbor)
#
#         return result
#
#
#
#     def dfs_util(self, node, visited, result):
#         visited[node] = True
#         result.append(node)
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.dfs_util(neighbor, visited, result)
#
#     def dfs(self, start):
#         visited = [False] * self.V
#         result = []
#         self.dfs_util(start, visited, result)
#         return result
#
#
#
#     def cyclic_util(self, node, visited, rec_stack):
#         visited[node] = True
#         rec_stack[node] = True
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor] and self.cyclic_util(neighbor, visited, rec_stack):
#                 return True
#             elif rec_stack[neighbor]:
#                 return True
#
#         rec_stack[node] = False
#         return False
#
#     def cyclic_detection(self):
#         visited = [False] * self.V
#         rec_stack = [False] * self.V
#
#         for node in range(self.V):
#             if not visited[node]:
#                 if self.cyclic_util(node, visited, rec_stack):
#                     return True
#         return False
#
#
#
#     def shortest_path(self, start):
#         dist = [float("inf")] * self.V
#         dist[start] = 0
#         queue = deque([start])
#
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.adj[node]:
#                 if dist[neighbor] == float("inf"):
#                     dist[neighbor] = dist[node] + 1
#                     queue.append(neighbor)
#
#         return dist
#
#
#
#     def topological_sort_util(self, node, visited, stack):
#         visited[node] = True
#
#         for neighbor in self.adj[node]:
#             if not visited[neighbor]:
#                 self.topological_sort_util(neighbor, visited, stack)
#
#         stack.append(node)
#
#     def topological_sort(self):
#         visited = [False] * self.V
#         stack = []
#         for node in range(self.V):
#             if not visited[node]:
#                 self.topological_sort_util(node, visited, stack)
#
#         return stack[::-1]



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)



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



    def shortest_path(self, start):
        dist = [float("inf")] * self.V
        dist[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if dist[neighbor] == float("inf"):
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        return dist



    def topological_path_util(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.topological_path_util(neighbor, visited, stack)
        stack.append(node)

    def topological_path(self, start):
        visited = [False] * self.V
        stack = []
        for node in range(self.V):
            if not visited[node]:
                self.topological_path_util(node, visited, stack)

        return stack[::-1]



    def cyclic_detection_util(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.adj[node]:
            if not visited[neighbor] and self.cyclic_detection_util(neighbor, visited, rec_stack):
                return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def cyclic_detection(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:
                if self.cyclic_detection_util(node, visited, rec_stack):
                    return True

        return False


