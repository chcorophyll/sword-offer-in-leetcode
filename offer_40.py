import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0 or k < 1 or k >len(arr):
            return []
        heap_queue = [-item for item in arr[:k]]
        heapq.heapify(heap_queue)
        for index in range(k, len(arr)):
            if -heap_queue[0] > arr[index]:
                heapq.heappop(heap_queue)
                heapq.heappush(heap_queue, -arr[index])
        result = [-item for item in heap_queue]
        return result