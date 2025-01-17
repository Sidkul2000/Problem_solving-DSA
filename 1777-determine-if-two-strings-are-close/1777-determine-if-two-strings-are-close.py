class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1 = set(word1)
        w2 = set(word2)
        # w1.sort()
        # w2.sort()
        if w1 != w2:
            return False
        c1 = list(Counter(word1).values())
        c2 = list(Counter(word2).values())
        return Counter(c1) == Counter(c2)

        # return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        