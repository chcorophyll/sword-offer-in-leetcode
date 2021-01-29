class Solution:
    # def get_first_index(self, nums, target, start, end):
    #     if start > end:
    #         return -1
    #     mid = start + (end - start) // 2
    #     if nums[mid] == target:
    #         if (mid > 0 and nums[mid-1] != target) or mid == 0:
    #             return mid
    #         else:
    #             end = mid -1
    #     elif nums[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #     return self.get_first_index(nums, target, start, end)

    # def get_last_index(self, nums, target, start, end):
    #     if start > end:
    #         return -1
    #     mid = start + (end - start) // 2
    #     if nums[mid] == target:
    #         if (mid < len(nums) - 1 and nums[mid+1] != target) or mid == len(nums) - 1:
    #             return mid
    #         else:
    #             start = mid + 1
    #     elif nums[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #     return self.get_last_index(nums, target, start, end)

    # def search(self, nums: List[int], target: int) -> int:
    # if not nums or target is None:
    #     return 0
    # first_index = self.get_first_index(nums, target, 0, len(nums)-1)
    # last_index = self.get_last_index(nums, target, 0, len(nums)-1)
    # count = 0
    # if first_index > -1 and last_index > -1:
    #     count += last_index - first_index + 1
    # return count
    def search(self, nums: [int], target: int) -> int:
        def get_right_index(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = i + (j - i) // 2
                if nums[mid] <= tar:
                    i = mid + 1
                else:
                    j = mid - 1
            return i

        return get_right_index(target) - get_right_index(target - 1)



