# < 6. Деревья >
# * Binary Tree Traversal: inorder, preorder, postorder.
from collections import deque

# -------------------------
# Структура узла дерева
# -------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -------------------------
# Класс BinaryTree с методами
# -------------------------
class BinaryTree:

    def __init__(self, root=None):
        self.root = root

# -------------------------
# Traversals
# -------------------------
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


# ----------------------------------------------------------------------


# -------------------------
# Maximum Depth
# -------------------------
    def max_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))


# ----------------------------------------------------------------------


# -------------------------
# Lowest Common Ancestor
# -------------------------
    def lowest_common_ancestor(self, node, p, q):
        """
        Возвращает узел LCA для узлов p и q
        """
        if not node or node == p or node == q:
            return node

        left = self.lowest_common_ancestor(node.left, p, q)
        right = self.lowest_common_ancestor(node.right, p, q)

        if left and right:
            return node
        return left or right


# ----------------------------------------------------------------------


# -------------------------
# Serialize / Deserialize
# -------------------------
    def serialize(self, node):
        """Сериализация дерева в строку (BFS)"""
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
                result.append("#")  # None placeholder
        return ",".join(result)

    def deserialize(self, data):
        """Десериализация строки в дерево (BFS)"""
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


# ----------------------------------------------------------------------


# -------------------------
# Пример использования
# -------------------------
if __name__ == "__main__":
    # Создадим дерево:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    tree = BinaryTree(root)

    # Traversals
    print("Inorder  :", tree.inorder(root))      # [4, 2, 5, 1, 3]
    print("Preorder :", tree.preorder(root))     # [1, 2, 4, 5, 3]
    print("Postorder:", tree.postorder(root))    # [4, 5, 2, 3, 1]

    # Max Depth
    print("Max depth:", tree.max_depth(root))    # 3

    # Lowest Common Ancestor
    lca = tree.lowest_common_ancestor(root, root.left.left, root.left.right)
    print("LCA of 4 and 5:", lca.val)           # 2

    # Serialize / Deserialize
    serialized = tree.serialize(root)
    print("Serialized tree:", serialized)

    deserialized_root = tree.deserialize(serialized)
    print("Inorder of deserialized tree:", tree.inorder(deserialized_root))