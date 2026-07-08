class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        n1 = [1]*len(nums)
        n2 = [1]*len(nums)
        for i in range(len(nums)):
            n1[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            # [1,2,3,4] => [1,1,2,6] => [24,12,4,1]
            n2[i] = postfix
            postfix *= nums[i]
        for i in range(len(n1)):
            n1[i] *= n2[i]
        return n1
