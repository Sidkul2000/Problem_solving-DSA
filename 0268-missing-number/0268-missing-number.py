class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [-1]*(n+1)
        for i in range(n):
            temp[nums[i]] = i
        for i in range(n+1):
            if temp[i] == -1:
                return i
        return 0
        