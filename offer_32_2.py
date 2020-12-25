# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # result = []
        # queue = [[root]]
        # while queue:
        #     current = queue.pop(0)
        #     level_result = []
        #     level_node = []
        #     for node in current:
        #         level_result.append(node.val)
        #         if node.left:
        #             level_node.append(node.left)
        #         if node.right:
        #             level_node.append(node.right)
        #     queue.append(level_node)
        #     result.append(level_result)
        # return result
        # if not root:
        #     return []
        # result = []
        # queue = collections.deque()
        # queue.append(root)
        # while root:
        #     level_result = []
        #     level_length = len(queue)
        #     for index in range(level_length):
        #         node = queue.popleft()
        #         level_result.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     result.append(level_result)
        # return result
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res