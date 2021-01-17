class Solution:

    def __init__(self):
        self.result = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.result += n
        return self.result