class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        counts = [0] * 32
        for num in nums:
            for i in range(32):
                counts[i] += num & 1
                num >>= 1
        res = 0
        for i in range(32):
            res <<= 1
            res |= (counts[31-i] % 3)
        return res if counts[31] == 0 else ~(res ^ 0xffffffff)