class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        smp = {}
        pmp = {}
        res = []

        for i in p:
            if i in pmp:
                pmp[i] += 1
            else:
                pmp[i] = 1

        l = 0
        for r in range(len(s)):
            if s[r] in smp:
                smp[s[r]] += 1
            else:
                smp[s[r]] = 1
            if (r-l+1) == len(p):
                if smp == pmp:
                    res.append(l)
                smp[s[l]] -= 1
                if smp[s[l]] == 0:
                    del smp[s[l]]
                l += 1
        return res