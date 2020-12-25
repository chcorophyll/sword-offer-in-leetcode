class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def check_more_than_half(nums_list, num_result):
            counts = 0
            for num in nums_list:
                if num == num_result:
                    counts += 1
            return 2 * counts > len(nums_list)

        if not nums:
            return None
        result = nums[0]
        counts = 1
        index = 1
        while index < len(nums):
            if counts == 0:
                result = nums[index]
                counts = 1
            elif nums[index] == result:
                counts += 1
            else:
                counts -= 1
            index += 1
        if check_more_than_half(nums, result):
            return result
        else:
            return None