# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            level_result = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(result) & 1:
                    level_result.appendleft(node.val)
                else:
                    level_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(level_result))
        return result