# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return None
#         queue = deque([root])
#         result = []
#         while queue:
#             current = queue.popleft()
#             result.append(current.val)
#             if root.left:
#                 queue.append(current.left)
#             else:
#                 result.append(None)
#             if root.right:
#                 queue.append(current.right)
#             else:
#                 result.append(None)
#         return result

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return None
#         root = TreeNode(data.poo(0))
#         queue = deque([root])
#         while data:
#             if queue:
#                 current = queue.popleft()
#                 if data.pop(0):
#                     current.left = TreeNode(data.pop(0))
#                     queue.append(current.left)
#                 if data.pop(0):
#                     current.right = TreeNode(data.pop(0))
#                     queue.append(current.left)
#         return root

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = deque([root])
        result = []
        while queue:
            current = queue.popleft()
            if current:
                result.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append("null")
        return "[" + ",".join(result) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        values, index = data[1:-1].split(","), 1
        root = TreeNode(int(values[0]))
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if values[index] != "null":
                current.left = TreeNode(int(values[index]))
                queue.append(current.left)
            index += 1
            if values[index] != "null":
                current.right = TreeNode(int(values[index]))
                queue.append(current.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))