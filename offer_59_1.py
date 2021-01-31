from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if not nums:
        #     return []
        # result = []
        # for i in range(len(nums)-k+1):
        #     result.append(max(nums[i:i+k]))
        # return result
        n = len(nums)
        result = []
        queue = deque()
        for i, j in zip(range(1-k, n-k+1), range(n)):
            if i > 0 and queue[0] == nums[i-1]:
                queue.popleft()
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            if i >= 0:
                result.append(queue[0])
        return result