class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        res = mx
        l, r = 1, mx

        while l <= r:
            mid = (l + r) // 2
            curr = 0
            for x in piles:
                curr += math.ceil(x / mid)
            if curr > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        
        return res