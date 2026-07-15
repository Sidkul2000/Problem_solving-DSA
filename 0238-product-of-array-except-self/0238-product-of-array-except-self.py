class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*n
        postf = [1]*n
        s = 1
        for i in range(n):
            pref[i] = s
            s *= nums[i]
        s = 1
        for i in range(n-1,-1,-1):
            postf[i] = s
            s *= nums[i]
        for i in range(n):
            nums[i] = pref[i]*postf[i]
        return nums