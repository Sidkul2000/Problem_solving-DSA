class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                mp[s[r]] += 1
            else:
                mp[s[r]] = 1
            if (r-l+1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res