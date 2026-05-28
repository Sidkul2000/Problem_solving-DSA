class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # we have to use stack no matter what
        stack = []
        temp = k
        res = ""
        if len(s)==0:
            return 0
        stack.append([s[0],1])
        for i in s[1:]:
            if stack and i==stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i,1])
        for i in stack:
            res += str(i[0])*i[1]
        return res
                


        