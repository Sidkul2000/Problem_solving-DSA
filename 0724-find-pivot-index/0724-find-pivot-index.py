class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n-1):
            left[i+1] = left[i] + nums[i]
        for i in range(n-1,0,-1):
            right[i-1] = right[i] + nums[i]
        for i in range(n):
            if (left[i] == right[i]):
                return i
        return -1 
        