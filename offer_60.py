class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        if n < 1:
            return None
        max_num = 6
        dp = [[0] * (max_num *n+1) for i in range(n+1)]
        for i in range(1, max_num+1):
            dp[1][i] = 1
        for k in range(2, n+1):
            for i in range(k):
                dp[k][i] = 0
            for j in range(k, k*max_num+1):
                for l in range(1, max_num+1):
                    if j - l >= 1:
                        dp[k][j] += dp[k-1][j-l]
        result = [dp[n][i] / 6 ** n for i in range(n, n*max_num+1)]
        return result