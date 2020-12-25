class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        index_left = 0
        root = postorder[-1]
        while postorder[index_left] < root:
            index_left += 1
        index_right = index_left
        while postorder[index_right] > root:
            index_right += 1
        if index_right < len(postorder) - 1:
            return False
        left = True
        if index_left > 0:
            left = self.verifyPostorder(postorder[0:index_left])
        right = True
        if index_right < len(postorder):
            right = self.verifyPostorder(postorder[index_left:index_right])
        return left and right