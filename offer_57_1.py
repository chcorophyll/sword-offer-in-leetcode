class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2 or not target:
            return []
        head = 0
        tail = len(nums) - 1
        while head < tail:
            current_sum = nums[head] + nums[tail]
            if  current_sum == target:
                break
            elif current_sum < target:
                head += 1
            else:
                tail -= 1
        if head < tail:
            return [nums[head], nums[tail]]
        else:
            return []