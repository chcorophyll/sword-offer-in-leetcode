class Solution:
    def permutation(self, s: str) -> List[str]:
        def recursive_string(temp_string):
            if not temp_string:
                return None
            string_length = len(temp_string)
            result = []
            first_string_set = set()
            for i in range(string_length):
                first_string = temp_string[i]
                if first_string in first_string_set:
                    continue
                else:
                    first_string_set.add(first_string)
                    next_recursive_string = temp_string[0:i] + temp_string[i+1:]
                    next_result = recursive_string(next_recursive_string)
                    if next_result:
                        for next_string in next_result:
                            string_pattern = "{}{}"
                            result.append(string_pattern.format(first_string, next_string))
                    else:
                        result.append(first_string)
            return result
        if not s:
            return None
        return recursive_string(s)