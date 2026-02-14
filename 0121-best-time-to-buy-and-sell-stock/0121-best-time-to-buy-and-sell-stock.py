class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = -9999
        p = prices[0]
        n = len(prices)
        if n==1:
            return 0
        for i in range(1,n):
            if prices[i] <= p:
                p = prices[i]
            maxp = max(maxp, prices[i] - p)
        return maxp
        