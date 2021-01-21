class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {" ": 0, "s": 1, "d": 2, ".": 4},
            {"d": 2, ".": 4},
            {"d": 2, ".": 3, "e": 5, " ": 8},
            {"d": 3, "e": 5, " ": 8},
            {"d": 3},
            {"s": 6, "d": 7},
            {"d": 7},
            {"d":7, " ": 8},
            {" ": 8}]
        p = 0
        for c in s:
            if "0" <= c <= "9":
                t = "d"
            elif c in "+-":
                t = "s"
            elif c in "eE":
                t = "e"
            elif c in ". ":
                t = c
            else:
                t = "?"
            if t not in states[p]:
                return False
            p = states[p][t]
        return p in (2, 3, 7, 8)