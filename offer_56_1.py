class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return None
        xor_num = functools.reduce(lambda x, y: x ^ y, nums)
        index = 1
        while index & xor_num == 0:
            index <<= 1
        num_0, num_1 = 0, 0
        for num in nums:
            if num & index:
                num_0 ^= num
            else:
                num_1 ^= num
        return [num_0, num_1]