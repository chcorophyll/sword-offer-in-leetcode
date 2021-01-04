class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        if  n == 0 or n == 1:
            return n
        f_a = 0
        f_b = 1
        i = 2
        while i <= n:
            f_c = f_b + f_a
            f_b, f_a = f_c, f_b
            i += 1
        return f_b % 1000000007