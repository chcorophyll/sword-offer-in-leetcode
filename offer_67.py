class Solution:
    def strToInt(self, str: str) -> int:
        s = str.strip()
        if not s:
            return 0
        result, index, sign = 0, 1, 1
        int_max, int_min, boundry_num = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if s[0] == "-":
            sign = -1
        elif s[0] != "+":
            index = 0
        for k in s[index:]:
            if not "0" <= k <= "9":
                break
            if result > boundry_num or (result == boundry_num and k > "7"):
                return int_max if sign == 1 else int_min
            result = result * 10 + ord(k) - ord("0")
        return result * sign