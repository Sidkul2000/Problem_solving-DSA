class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1
        for n in nums:
            temp1 = currMax*n
            temp2 = currMin*n
            currMax = max(temp1, temp2, n)
            currMin = min(temp1, temp2, n)

            res = max(currMax, res)

        return res

        
