class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = [1]*len(nums)
        for i in range(len(nums)):
            n[i] = prefix
            prefix *= nums[i]
        for i in range(len(n)-1, -1, -1):
            n[i] *= postfix
            postfix *= nums[i]
        return n




