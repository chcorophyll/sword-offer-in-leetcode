class Solution:
    def replaceSpace(self, s: str) -> str:
        # length = len(s)
        # if length == 0:
        #     return None
        # space_count = 0
        # for i in range(length):
        #     if s[i] == "  ":
        #         space_count += 1
        # new_length = length + 2 * space_count
        # index = length - 1
        # new_index = new_length - 1
        if len(s) == 0:
            return ""
        result = []
        for i in s:
            if i == " ":
                result.append("%")
                result.append("2")
                result.append("0")
            else:
                result.append(i)
        return "".join(result)