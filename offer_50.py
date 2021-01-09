class Solution:
    def firstUniqChar(self, s: str) -> str:
        # if not s:
        #     return " "
        # letter_counts = {}
        # for letter in s:
        #     if not letter in letter_counts:
        #         letter_counts[letter] = 1
        #     else:
        #         letter_counts[letter] += 1
        # for letter, value in letter_counts.items():
        #     if value == 1:
        #         return letter
        # return " "
        if not s:
            return " "
        letter_counts = {}
        for letter in s:
            letter_counts[letter] = not letter in letter_counts
        for letter, count in letter_counts.items():
            if count:
                return letter
        return " "
