class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        def func(x, rev):
            if x == 0:
                return rev
            if x > 0:
                rem = x % 10
            else:
                rem = x % 10
            x = x//10
            rev = rev*10 + rem
            return func(x, rev)
        rev = sign * func(x, 0)
        return rev if -(2**31) <= rev <= (2**31 - 1) else 0
        