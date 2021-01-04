# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def tree_in_tree(tree_0, tree_1):
            if tree_1 is None:
                return True
            if tree_0 is None:
                return False
            if tree_0.val != tree_1.val:
                return False
            return tree_in_tree(tree_0.left, tree_1.left) and tree_in_tree(tree_0.right, tree_1.right)
        result = False
        if A and B:
            if A.val == B.val:
                result = tree_in_tree(A, B)
            if not result:
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)
        return result