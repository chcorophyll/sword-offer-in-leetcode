class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if not isinstance(target, int):
            return False
        stop = False
        i = 0
        j = len(matrix[0]) - 1
        while (i < len(matrix) and j >= 0) and not stop:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                stop = True
        return stop