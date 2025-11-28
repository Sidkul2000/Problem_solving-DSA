class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for i, char in enumerate(s):
            if d[char] == 1:
                return i
        return -1

        


        
        