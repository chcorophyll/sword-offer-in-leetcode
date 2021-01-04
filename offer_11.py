class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # if not numbers:
        #     return None
        # head_index = 0
        # tail_index = len(numbers) - 1
        # mid_index = 0
        # while numbers[head_index] >= numbers[tail_index]:
        #     if tail_index - head_index == 1:
        #         break
        #     if numbers[head_index] == numbers[mid_index] and numbers[mid_index] == numbers[tail_index]:
        #         for i in range(tail_index+1):
        #             if numbers[head_index] > numbers[i]:
        #                 return numbers[i]
        #     mid_index = (head_index + tail_index) // 2
        #     if numbers[head_index] <= numbers[mid_index]:
        #         head_index = mid_index
        #     elif numbers[tail_index] >= numbers[mid_index]:
        #         tail_index = mid_index

        # return numbers[mid_index]
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] == numbers[right]:
                right -= 1
        return numbers[left]