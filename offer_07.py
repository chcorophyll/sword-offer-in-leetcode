# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != 0 and len(preorder) == len(inorder):
            root_value = preorder[0]
            if root_value in inorder:
                left_right_index = inorder.index(root_value)
                if len(preorder[:left_right_index]) != 0:
                    left_tree = self.buildTree(preorder[1:left_right_index+1], inorder[:left_right_index])
                else:
                    left_tree = None
                if len(preorder[left_right_index+1:]) != 0:
                    right_tree = self.buildTree(preorder[left_right_index+1:], inorder[left_right_index+1:])
                else:
                    right_tree = None
                return TreeNode(root_value, left_tree, right_tree)