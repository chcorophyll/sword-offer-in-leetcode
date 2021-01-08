class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # def is_ugly(number):
        #     while number % 2 == 0:
        #         number = number / 2
        #     while number % 3 == 0:
        #         number = number / 3
        #     while number % 5 == 0:
        #         number = number / 5
        #     return number == 1
        # if n < 1:
        #     return None
        # index = 0
        # current_number = 0
        # while index < n:
        #     current_number += 1
        #     if is_ugly(current_number):
        #         index += 1
        # return current_number
        # if n < 1:
        #     return None
        # ugly_numbers = [1]
        # index = 0
        # index_2 = 0
        # index_3 = 0
        # index_5 = 0
        # while index < n:
        #     while 2 * ugly_numbers[index_2] <= ugly_numbers[index]:
        #         index_2 += 1
        #     while 3 * ugly_numbers[index_3] <= ugly_numbers[index]:
        #         index_3 += 1
        #     while 5 * ugly_numbers[index_5] <= ugly_numbers[index]:
        #         index_5 += 1
        #     current_min = min(2 * ugly_numbers[index_2], 3 * ugly_numbers[index_3], 5 * ugly_numbers[index_5])
        #     ugly_numbers.append(current_min)
        #     index += 1
        # return ugly_numbers[index-1]
        if n < 1:
            return None
        dp = [1] * n
        index_2 = 0
        index_3 = 0
        index_5 = 0
        for index in range(1, n):
            num_2 = 2 * dp[index_2]
            num_3 = 3 * dp[index_3]
            num_5 = 5 * dp[index_5]
            dp[index] = min(num_2, num_3, num_5)
            if dp[index] == num_2:
                index_2 += 1
            if dp[index] == num_3:
                index_3 += 1
            if dp[index] == num_5:
                index_5 += 1
        return dp[-1]