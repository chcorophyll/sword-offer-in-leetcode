class Solution:

    # def reverse(self, s, head_index, tail_index):
    #     while head_index < tail_index:
    #         if head_index+1 < tail_index:
    #             s = s[tail_index] + s[head_index+1: tail_index] + s[head_index]
    #             head_index += 1
    #             tail_index -= 1

    # def reverseLeftWords(self, s: str, n: int) -> str:
    #     if not s or not n or n > len(s):
    #         return None
    #     first_start = 0
    #     first_end = first_start + n - 1
    #     second_start = n
    #     second_end = len(s) -1
    #     self.reverse(s, first_start, first_end)
    #     self.reverse(s, second_start, second_end)
    #     self.reverse(s, first_start, second_end)

    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s or not n or n > len(s):
            return None
        result = []
        for i in range(n, n+len(s)):
            result.append(s[i % len(s)])
        return "".join(result)