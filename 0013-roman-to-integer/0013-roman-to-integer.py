class Solution:
    def romanToInt(self, s: str) -> int:
        if s == "":
            return 0
        result = 0
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        for n in range(len(s)):
            if n+1 < len(s) and roman[s[n]] < roman[s[n+1]]:
                result -= roman[s[n]]
            else:
                result += roman[s[n]]
        return result
            



        