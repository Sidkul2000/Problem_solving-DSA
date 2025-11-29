class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxprof = 0
        for p in prices:
            if p <= minp:
                minp = p
            else:
                maxprof = max(maxprof, p - minp)
        return maxprof