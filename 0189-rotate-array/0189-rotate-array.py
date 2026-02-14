class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        temp = nums.copy()
        for i in range(k):
            nums[i] = temp[n-k+i]
        for i in range(k, n):
            nums[i] = temp[i-k]