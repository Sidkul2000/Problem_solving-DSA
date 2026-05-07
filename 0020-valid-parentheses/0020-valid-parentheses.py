class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return False
        stack = []
        for i in s:
            if i != ")" and i != "]" and i != "}":
                stack.append(i)
            else:
                if not stack:
                    return False
                st = stack.pop()
                if i==")" and st != "(":
                    return False
                if i=="]" and st != "[":
                    return False
                if i=="}" and st != "{":
                    return False
        if not stack:
            return True
        else:
            return False
            