class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target < 3:
            return []
        mid = (target + 1) / 2
        small = 1
        big = 2
        current_sum = small + big
        res = []
        while small < mid:
            if current_sum > target:
                current_sum -= small
                small += 1
            elif current_sum < target:
                big += 1
                current_sum += big
            else:
                res.append([i for i in range(small, big+1)])
                big += 1
                current_sum += big
        return res