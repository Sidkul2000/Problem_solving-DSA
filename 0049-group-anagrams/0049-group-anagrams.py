class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        mp = {}
        for i in strs:
            s = sorted(i)
            k = tuple(s)
            if k not in mp:
                mp[k] = [i]
            else:
                mp[k].append(i)
        return list(mp.values())
            