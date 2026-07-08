class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l, r = max(weights), sum(weights)
        while l<r:
            m = (l+r)//2
            d = 1
            w = 0
            for i in range(n):
                if w+weights[i] > m:
                    w = 0
                    d += 1
                w += weights[i]
            if d > days:
                l = m + 1
            else:
                r = m
        return r 