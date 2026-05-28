class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n==1:
            return n
        c = chars[0]
        s = 1
        for i in range(1,n):
            if chars[i] == chars[i-1]:
                s+=1
            else:
                if s>1:
                    c += str(s)
                    s=1
                c += chars[i]
        if s>1:
            c += str(s)
        for i in range(len(c)):
            chars[i] = c[i]
        return len(c)



