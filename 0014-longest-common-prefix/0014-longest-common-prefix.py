class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        n = len(first)
        for w in strs[1:]:
            while first != w[0:n]:
                n -= 1
                if n==0:
                    return ""
                first = first[0:n]
        return first
        
