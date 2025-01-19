class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                string *= num

                stack.append(string)
        return "".join(stack)
            
            


                

        