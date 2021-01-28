class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        position_record = {}
        result, temp = 0, 0
        for j in range(len(s)):
            i = position_record.get(s[j], -1)
            position_record[s[j]] = j
            temp = temp + 1 if temp < j - i else j - i
            result = max(result, temp)
        return result