class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1]==n:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                if n+nums[l]+nums[r] > 0:
                    r -= 1
                elif n+nums[l]+nums[r] < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return ans