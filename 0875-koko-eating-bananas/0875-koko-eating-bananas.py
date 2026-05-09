class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            s = sum((p-1)//speed+1 for p in piles)
            if s <= h:
                return True
            else:
                return False

        n = len(piles)
        l, r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l