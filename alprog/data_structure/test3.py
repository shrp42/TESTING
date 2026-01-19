# LESSON 5/6:
from collections import *

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


