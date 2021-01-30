# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            if self.k == 0:
                return None
            self.k -= 1
            if self.k == 0:
                self.result = root.val
            dfs(root.left)
        self.k = k
        self.result = None
        dfs(root)
        return self.result