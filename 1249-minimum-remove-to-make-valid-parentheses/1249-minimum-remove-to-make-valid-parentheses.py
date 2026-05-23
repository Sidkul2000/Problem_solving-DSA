class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = []
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                if stack:
                    stack.pop()
                else:
                    invalid.append(i)
        while stack:
            invalid.append(stack.pop())
        res = []
        for i in range(len(s)):
            if i in invalid:
                continue
            res.append(s[i])
        return "".join(res)