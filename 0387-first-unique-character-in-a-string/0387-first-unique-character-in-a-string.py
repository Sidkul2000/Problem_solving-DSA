class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        if len(s)==0:
            return -1
        for i in s:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for i in range(len(s)):
            if mp[s[i]]==1:
                return i
        return -1