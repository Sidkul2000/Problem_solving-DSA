class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        count = 0
        sum = 0
        partsum = 0
        for i in range(n):
            sum += nums[i]
        for i in range(n-1):
            partsum += nums[i]
            sum -= nums[i]
            if (sum - partsum) % 2 == 0:
                count += 1
        return count

            


        