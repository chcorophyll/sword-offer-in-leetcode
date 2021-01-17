class Solution:
    def add(self, a: int, b: int) -> int:
        # x = 0xffffffff
        # a = a & x
        # b = b & x
        # while b != 0:
        #     a = a ^ b
        #     b = (a & b) << 1
        # return a if a < x else ~(a ^ x)
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)