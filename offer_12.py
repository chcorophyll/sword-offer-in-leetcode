class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not (0<=i<len(board)) or not(0<=j<len(board[0])) or board[i][j] != word[k]:
                return False
            if len(word) - 1 == k:
                return True
            board[i][j] = " "
            result = dfs(i, j+1, k+1) or dfs(i, j-1, k+1) or dfs(i-1, j, k+1) or dfs(i+1, j, k+1)
            board[i][j] = word[k]
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False