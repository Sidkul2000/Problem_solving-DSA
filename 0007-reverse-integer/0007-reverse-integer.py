class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        x = x*sign
        
        if x == 1 or x == 0:
            return x*sign
        rev = 0
        while x != 0:
            rev = rev*10 + x % 10
            x = x//10
        if rev >= 2**31:
            return 0
        return rev*sign
        

        