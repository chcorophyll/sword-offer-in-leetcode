class Solution:
    def merge_sort(self, nums, temp_nums, start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        count = self.merge_sort(nums, temp_nums, start, mid) + self.merge_sort(nums, temp_nums, mid+1, end)
        i, j, pos = start, mid+1, start
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp_nums[pos] = nums[i]
                count += (j - (mid + 1))
                i += 1
            else:
                temp_nums[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid+1):
            temp_nums[pos] = nums[k]
            count += (j - (mid + 1))
            pos += 1
        for k in range(j, end+1):
            temp_nums[pos] = nums[k]
            pos += 1
        nums[start:end+1] = temp_nums[start:end+1]
        return count

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp_nums = [0] * len(nums)
        return self.merge_sort(nums, temp_nums, 0, len(nums)-1)