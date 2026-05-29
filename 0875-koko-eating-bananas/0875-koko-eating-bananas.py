class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        count = 0
        minc = r
        while l<=r:
            mid = (l+r)//2
            count = 0
            for i in range(n):
                count += ((piles[i]-1)//mid) + 1
            if count > h:
                l = mid + 1
            else:
                r = mid - 1
                minc = min(minc, mid)
        return minc