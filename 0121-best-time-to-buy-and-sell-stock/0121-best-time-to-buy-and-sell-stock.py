class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = -9999
        l = 0
        n = len(prices)
        if n==1:
            return 0
        for r in range(1,n):
            if prices[r] <= prices[l]:
                l = r
            s = prices[r] - prices[l]
            maxp = max(maxp, s)
        return maxp
