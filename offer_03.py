class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # length = len(nums)
        # if length == 0:
        #     return None
        # for i in range(length):
        #     if nums[i] == nums[nums[i]]:
        #         return nums[i]
        #     while i != nums[i]:
        #         nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        #     i += 1
        # return None
        length = len(nums)
        count_list = [0] * length
        for i in range(length):
            count_list[nums[i]] += 1
            if count_list[nums[i]] > 1:
                return nums[i]
        return None