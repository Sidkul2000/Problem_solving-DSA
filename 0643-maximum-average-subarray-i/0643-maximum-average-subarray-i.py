class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum1 = 0
        for i in range(k):
            sum1 += nums[i]
        count = 0
        maxim = sum1
        for i in range(n-k):
            sum1 = sum1 - nums[i] + nums[i+k]
            if sum1 > maxim:
                maxim = sum1
        return (float(maxim/k))

        

        