class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sortedNums = sorted(nums)
        if nums==sortedNums:
            return 0
        left, right = 0, n-1
        while left < n and nums[left]==sortedNums[left]:
            left+=1
        while right >= 0 and nums[right]==sortedNums[right]:
            right-=1
        if left > right:
            return 0

        return (right-left+1)
        