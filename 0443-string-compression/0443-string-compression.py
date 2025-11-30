class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        n = len(chars)
        s = ""
        cnt = 1
        temp = chars[0]
        for i in range(1, n):
            if chars[i] != temp:
                temp = chars[i]
                s = s + chars[i-1]
                if cnt != 1:
                    s = s + str(cnt)
                cnt = 1
            else:
                cnt += 1
        s += chars[n-1]
        if cnt != 1:
            s += str(cnt)
        for i, char in enumerate(s):
            chars.insert(i, char)
        return len(s)

