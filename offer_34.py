# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def find_path(current_root, expected_sum, current_path, current_sum):
            current_sum += current_root.val
            current_path.append(current_root.val)
            leaf_check = False
            if current_root.left is None and current_root.right is None:
                leaf_check = True
            if current_sum == expected_sum and leaf_check:
                result.append(list(current_path))
            if current_root.left:
                find_path(current_root.left, expected_sum, current_path, current_sum)
            if current_root.right:
                find_path(current_root.right, expected_sum, current_path, current_sum)
            current_sum -= current_root.val
            current_path.pop()
        if not root:
            return []
        result = []
        orignal_path = collections.deque()
        original_sum = 0
        find_path(root, sum, orignal_path, original_sum)
        return result