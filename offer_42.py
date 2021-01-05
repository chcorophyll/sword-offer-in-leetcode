class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return None
        # current_sum = 0
        # greatest_sum = -float("inf")
        # for num in nums:
        #     if current_sum < 0:
        #         current_sum = num
        #     else:
        #         current_sum += num
        #     if current_sum > greatest_sum:
        #         greatest_sum = current_sum
        # return greatest_sum
        # if not nums:
        #     return None
        # dp = [-float("inf")] * (len(nums) + 1)
        # for index in range(1, len(nums)+1):
        #     if dp[index-1] < 0:
        #         dp[index] = nums[index-1]
        #     else:
        #         dp[index] = dp[index-1] + nums[index-1]
        # return max(dp)
        if not nums:
            return None
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)