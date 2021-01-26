class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        a, b = 1, 1
        for i in range(2, len(num_str)+1):
            a, b = b, (a + b if "10" <= num_str[i-2:i] <= "25" else b)
        return b