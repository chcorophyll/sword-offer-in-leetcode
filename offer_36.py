"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # def tree_to_node_list(node, tail_node):
        #     if not node:
        #         return None
        #     current_node = node
        #     if current_node.left:
        #         tail_node = tree_to_node_list(current_node.left, tail_node)
        #     current_node.left = tail_node
        #     if tail_node:
        #         tail_node.right = current_node
        #     tail_node = current_node
        #     if current_node.right:
        #         tail_node = tree_to_node_list(current_node.right, tail_node)
        #     return tail_node
        # tail_result = tree_to_node_list(root, None)
        # head_node = tail_result
        # while head_node and head_node.left:
        #     head_node = head_node.left
        # return head_node
        def dfs(current_node):
            if not current_node:
                return None
            dfs(current_node.left)
            if self.tail_node:
                self.tail_node.right, current_node.left = current_node, self.tail_node
            else:
                self.head_node = current_node
            self.tail_node = current_node
            dfs(current_node.right)
        if not root:
            return None
        self.tail_node = None
        dfs(root)
        self.head_node.left, self.tail_node.right = self.tail_node, self.head_node
        return self.head_node