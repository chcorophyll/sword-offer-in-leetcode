class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0:
        #     return 1
        # else:
        #     if n == 0:
        #         return 1
        #     elif n < 0:
        #         exponent = -n
        #     else:
        #         exponent = n
        #     product = 1
        #     while exponent > 0:
        #         product = product * x
        #         exponent -= 1
        #     if n < 0:
        #         product = 1 / product
        #     return product
        def recursive_product(base, positive_exponent):
            if positive_exponent == 0:
                return 1
            if positive_exponent == 1:
                return base
            r_product = recursive_product(base, positive_exponent >> 1)
            r_product *= r_product
            if positive_exponent & 1:
                r_product *= base
            return r_product
        if x == 0:
            return 1
        else:
            if n < 0:
                exponent = -n
            else:
                exponent = n
            product = recursive_product(x, exponent)
            if n < 0:
                product =  1 / product
            return product