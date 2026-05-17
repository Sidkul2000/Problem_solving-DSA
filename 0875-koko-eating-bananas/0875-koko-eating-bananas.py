class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r:
            s=0
            mid = (l+r)//2
            for i in piles:
                s += int((i-1)/mid + 1)
            if s <= h:
                r = mid-1
            elif s > h:
                l = mid+1
    
        return l
        