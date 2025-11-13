class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = maxi = 0
        n = len(s)
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxi = max(maxi, r - l + 1)
        
        return maxi
