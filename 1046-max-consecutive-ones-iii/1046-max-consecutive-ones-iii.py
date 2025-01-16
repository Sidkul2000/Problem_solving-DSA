class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        front = 0
        back = 0
        while (front < n):
            if (nums[front] == 0):
                k -= 1
            front += 1
            if k < 0:
                if nums[back] == 0:
                    k += 1
                back += 1
        return front - back


