class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        c_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for i in t:
            if i in c_dict:
                c_dict[i] += 1
            else:
                c_dict[i] = 1

        if s_dict == c_dict:
            return True
        else:
            return False
        