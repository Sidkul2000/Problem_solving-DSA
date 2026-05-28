class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        price = prices[0]
        for i in prices[1:]:
            if i < price:
                price = i
            else:
                maxp = max(maxp, i-price)
        return maxp
