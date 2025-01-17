class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        k = 1
        while (j < n):
            if nums[j] == 0:
                k -= 1
            j += 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return (j - i - 1)
