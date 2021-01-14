class Solution:
    # def strip_blank(self, s, head_index, tail_index):
    #     if not s or not head_index or not tail_index:
    #         return None
    #     while s[head_index] == " ":
    #         head_index += 1
    #     while s[tail_index] == " ":
    #         tail_index -= 1
    #     start_index = head_index
    #     end_index = head_index
    #     result = []
    #     while start_index != tail_index + 1:
    #         if s[head_index] == " ":
    #             start_index += 1
    #             end_index += 1
    #         elif s[end_index] == " " or s[end_index] == len(s) -1:
    #             if s[end_index] == " ":
    #                 result.append(s[start_index:end_index])
    #                 start_index += end_index
    #             else:
    #                 result.append(s[start_index:end_index+1])
    #                 start_index += (end_index + 1)
    #         else:
    #             end_index += 1
    #     return " ".join(result)

    # def reverse(self, s, head_index, tail_index):
    #     if not s or not head_index or not tail_index:
    #         return None
    #     while head_index < tail_index:
    #         s[head_index], s[tail_index] = s[tail_index], s[head_index]
    #         head_index += 1
    #         tail_index -= 1

    # def reverseWords(self, s: str) -> str:
    #     if not s:
    #         return None
    #     head_index, tail_index = 0, len(s)-1
    #     s = self.strip_blank(s, head_index, tail_index)
    #     head_index, tail_index = 0, len(s)-1
    #     self.reverse(s, head_index, tail_index)
    #     start_index = 0
    #     end_index = 0
    #     while start_index != len(s):
    #         if s[start_index] == " ":
    #             start_index += 1
    #             end_index += 1
    #         elif s[end_index] == " " or s[end_index] == len(s) -1:
    #             if s[end_index] == " ":
    #                 self.reverse(s, start_index, end_index-1)
    #                 start_index += end_index
    #             else:
    #                 self.reverse(s, start_index, end_index)
    #                 start_index += (end_index + 1)
    #         else:
    #             end_index += 1
    #     return s
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = len(s) - 1
        j = i
        result = []
        while i >= 0:
            while s[i] != " " and i >= 0:
                i -= 1
            result.append(s[i + 1: j + 1])
            while s[i] == " ":
                i -= 1
            j = i
        return " ".join(result)
