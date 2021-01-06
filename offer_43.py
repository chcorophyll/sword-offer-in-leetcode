class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, result = 1, 0
        high, current, low = n // 10, n % 10, 0
        while high != 0 or current != 0:
            if current == 0:
                result += high * digit
            elif current == 1:
                result += high * digit + low + 1
            else:
                result += (high + 1) * digit
            low += current * digit
            current = high % 10
            high //= 10
            digit *= 10
        return result