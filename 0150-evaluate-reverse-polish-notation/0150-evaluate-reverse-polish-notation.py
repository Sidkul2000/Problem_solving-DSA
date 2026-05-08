class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans=0
        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                stack.append(int(i))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i=="+":
                    ans = a+b
                elif i=="-":
                    ans = b-a
                elif i=="*":
                    ans = a*b
                elif i=="/":
                    ans = int(b/a)
                stack.append(int(ans))
        return stack[0]
        