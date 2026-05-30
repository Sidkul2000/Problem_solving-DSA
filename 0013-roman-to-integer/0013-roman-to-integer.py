class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0

        for n in range(len(s)):
            if n+1 < len(s) and mp[s[n]] < mp[s[n+1]]:
                num -= mp[s[n]]
            else:
                num += mp[s[n]]
        return num
