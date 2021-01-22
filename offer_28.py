# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recursive(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return recursive(left.left, right.right) and recursive(left.right, right.left)
        return recursive(root.left, root.right) if root else True