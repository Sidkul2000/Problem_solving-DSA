class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(temp - target) < abs(target - res):
                    res = temp
                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
                else:
                    return target
        return res