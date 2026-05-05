class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        if x<0:
            return False
        if x < 10:
            return True
        temp = x
        while(x > 0):
            rev = rev*10 + x%10
            x = x//10
        if temp == rev:
            return True
        else:
            return False
