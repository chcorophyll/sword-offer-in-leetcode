from collections import deque


class Solution:
    
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return -1
        # queue = deque()
        # for i in range(n):
        #     queue.append(i)
        # while len(queue) > 1:
        #     index = 0
        #     while index < m-1:
        #         queue.append(queue.popleft())
        #     queue.popleft()
        # return queue.pop()
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last