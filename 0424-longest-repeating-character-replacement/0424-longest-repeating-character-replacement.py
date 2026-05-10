class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        res = 0
        mp = {}
        for r in range(n):
            if s[r] in mp:
                mp[s[r]] += 1
            else:
                mp[s[r]] = 1
            maxf = max(mp.values())
            curr = r - l + 1
            if curr - maxf > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


        