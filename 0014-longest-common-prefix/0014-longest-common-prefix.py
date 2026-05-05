class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        n = len(first)
        for word in strs[1:]:
            while first != word[0:n]:
                n -= 1
                if n == 0:
                    return ""
                first = first[0:n]
        return first[0:n]


        
