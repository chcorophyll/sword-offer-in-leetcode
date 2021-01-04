class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def anticlock_traverse(nums, rows, cols, start):
            end_x = rows - start
            end_y = cols - start
            for i in range(start, end_y):
                result.append(nums[start][i])
            if start < end_x -1:
                for i in range(start+1, end_x):
                    result.append(nums[i][end_y-1])
            if start < end_x -1 and start < end_y -1:
                for i in range(end_y-2, start-1, -1):
                    result.append(nums[end_x-1][i])
            if start < end_x -2 and start < end_y -1:
                for i in range(end_x-2, start, -1):
                    result.append(nums[i][start])
        if matrix is None:
            return []
        result = []
        matrix_rows = len(matrix)
        if matrix_rows <= 0:
            return result
        matrix_cols = len(matrix[0])
        if matrix_cols <= 0:
            return result
        start = 0
        while (matrix_rows > 2 * start) and (matrix_cols > 2 * start):
            anticlock_traverse(matrix, matrix_rows, matrix_cols, start)
            start += 1
        return result