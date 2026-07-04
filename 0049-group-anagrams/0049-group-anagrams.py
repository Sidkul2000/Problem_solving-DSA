class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            w = "".join(sorted(s))
            if w in mp:
                mp[w].append(s)
            else:
                mp[w] = [s]
        return list(mp.values())