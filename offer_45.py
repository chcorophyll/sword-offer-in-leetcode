class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(left, right):
            if left > right:
                return None
            i, j = left, right
            while i < j:
                while str_list[j] + str_list[left] >= str_list[left] + str_list[j] and i < j:
                    j -= 1
                while str_list[i] + str_list[left] <= str_list[left] + str_list[i] and i < j:
                    i += 1
                if i < j:
                    str_list[i], str_list[j] =str_list[j], str_list[i]
            str_list[left], str_list[j] = str_list[j], str_list[left]
            quick_sort(left, j-1)
            quick_sort(j+1, right)
        if not nums:
            return None
        str_list = [str(num) for num in nums]
        quick_sort(0, len(str_list)-1)
        return "".join(str_list)