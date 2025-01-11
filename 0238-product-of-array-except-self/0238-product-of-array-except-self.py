class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [1] * n
        prod = 1
        for i in range(n):
            temp[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            temp[i] *= prod
            prod *= nums[i]

        return temp