class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n%3 != 0:
            return False
        while n%3 == 0:
            if n/3==1:
                return True
            n = n/3
        return False
