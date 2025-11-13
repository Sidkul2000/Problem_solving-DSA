class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) - 1
        maxstr = s[0]
        if len(s) <= 1:
            return s
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(maxstr):
                maxstr = odd
            if len(even) > len(maxstr):
                maxstr = even
        return maxstr
