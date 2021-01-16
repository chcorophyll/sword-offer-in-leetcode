import random


class Solution:

    # def quick_sort(self, nums, left, right):
    #     if left > right:
    #         return None
    #     # index = random.randrange(left, right)
    #     # nums[index], nums[left] = nums[left], nums[index]
    #     else:
    #         current_num = nums[left]
    #         low = left + 1
    #         high = right
    #         while low <= high:
    #             while nums[low] <= current_num and low <= high:
    #                 low += 1
    #             while nums[high] > current_num and low <= high:
    #                 high -= 1
    #             if low <= high:
    #                 nums[low], nums[high] = nums[high], nums[low]
    #         nums[left], nums[high] = nums[high], nums[left]
    #         self.quick_sort(nums, left, high-1)
    #         self.quick_sort(nums, high+1, right)

    def isStraight(self, nums: List[int]) -> bool:
        # if not nums:
        #     return False
        # nums.sort()
        # zero_counts = 0
        # index = 0
        # while index < len(nums):
        #     if nums[index] == 0:
        #         zero_counts += 1
        #         index += 1
        #     else:
        #         break
        # gap_counts = 0
        # small = index
        # big = small + 1
        # while big < len(nums):
        #     if nums[small] == nums[big]:
        #         return False
        #     gap_counts += nums[big] - nums[small] - 1
        #     small = big
        #     big += 1
        # return zero_counts >= gap_counts
        jokes = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                jokes += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[jokes] < 5


