class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = "aeiouAEIOU"
        end = len(s)-1
        start = 0
        s = list(s)
        while start < end:
            if s[start] in vow and s[end] in vow:
                temp = s[end]
                s[end] = s[start]
                s[start] = temp
                start += 1
                end -= 1
            elif s[start] in vow and s[end] not in vow:
                end -= 1
            elif s[start] not in vow and s[end] in vow:
                start += 1
            elif s[start] not in vow and s[end] not in vow:
                start += 1
                end -= 1
        return "".join(s)


        