class Solution:
    def numWays(self, n: int) -> int:
        # if n == 1 or n == 2:
        #     return n
        # return (self.numWays(n-1) + self.numWays(n-2)) % 1000000007
        a, b = 1, 1
        for _ in range(n-1):
            a, b = a+b, a
        return  a % 1000000007