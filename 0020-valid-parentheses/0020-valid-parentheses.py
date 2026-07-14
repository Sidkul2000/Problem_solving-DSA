class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or stack[-1] != mp[i]:
                    return False
                stack.pop()
        if stack:
            return False
        return True

