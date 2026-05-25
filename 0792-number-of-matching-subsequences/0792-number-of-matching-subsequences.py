class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        cache = {}
        def isSubsequence(s,word):
            i = 0
            for w in s:
                if i==len(word):
                    return True
                if w == word[i]:
                    i+=1
            if i==len(word):
                return True
            else:
                return False
        for i in words:
            if i not in cache:
                cache[i] = isSubsequence(s,i)
            if cache[i]:
                count += 1
        return count

        