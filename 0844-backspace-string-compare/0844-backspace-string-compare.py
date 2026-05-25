class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp1, temp2 = [], []
        for i in range(len(s)):
            if s[i] == "#":
                if temp1:
                    temp1.pop()
            else:
                temp1.append(s[i])

        for i in range(len(t)):
            if t[i] == "#":
                if temp2:
                    temp2.pop()
            else:
                temp2.append(t[i])

        return temp1 == temp2
        