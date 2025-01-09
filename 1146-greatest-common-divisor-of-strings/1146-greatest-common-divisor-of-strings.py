class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        a = len(str1)
        b = len(str2)
        while (b):
            temp = b
            b = a % b 
            a = temp

        return str1[:a]

            
