class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        ans = []

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str in ana:
                ans[ana[sorted_str]].append(s)
            else:
                ana[sorted_str] = len(ans)
                ans.append([s])

        return ans



