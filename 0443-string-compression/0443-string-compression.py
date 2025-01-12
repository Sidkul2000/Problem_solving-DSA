class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        s = ""
        i, j = 0, 1
        c = 0
        while j<n:
            if (chars[i] == chars[j]):
                j+=1
                c+=1
            elif c == 0:
                s = s + chars[i]
                i+=1
                j+=1
            else:
                s = s + chars[i] + str(j-i)
                i = j
                j+=1
                c = 0
        if (j-i) != 1:
            s = s + chars[i] + str(j-i)
        else:
            s = s + chars[i]
        for i in range(len(s)):
            chars[i] = s[i]
        chars = chars[:len(s)]
        return len(chars)
        