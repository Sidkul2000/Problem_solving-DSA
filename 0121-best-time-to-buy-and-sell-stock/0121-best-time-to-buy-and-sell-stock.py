class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = -9999
        l = prices[0]
        n = len(prices)
        if n==1:
            return 0
        for r in prices[1:]:
            l = min(l,r)
            s = r - l
            maxp = max(maxp, s)
        return maxp
