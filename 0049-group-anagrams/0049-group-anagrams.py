class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in mp:
                mp[s].append(i)
            else:
                mp[s] = [i]
        return list(mp.values())
        