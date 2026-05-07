class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # c = 0
        # if len(s) != len(t):
        #     return False
        # for i in s:
        #     if i in t:
        #         c += 1
        # if c == len(s) == len(t):
        #     return True
        # else:
        #     return False
        s = sorted(s)
        t = sorted(t)
        if s==t:
            return True
        else:
            return False
        