import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n):
            for j in range(i+1, n):
                sq = math.sqrt(i**2 + j**2)
                if sq <= n and sq == int(sq):
                    count += 2
        return count