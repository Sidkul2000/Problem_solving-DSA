class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        num = 0
        n = len(s)
        for i in range(k):
            if s[i] in vowel:
                num += 1
        if num == k:
            return num
        maxim = num
        counter = 0
        for i in range(k, n):
            if s[counter] in vowel:
                num -= 1
                counter += 1
            else:
                counter += 1
            if s[i] in vowel:
                num += 1
            if num >= maxim:
                maxim = num
    
        return maxim
        