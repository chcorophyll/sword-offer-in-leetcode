class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for i in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == ".")
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1])
        return dp[-1][-1]