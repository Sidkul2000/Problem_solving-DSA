class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        back = 0
        for front in range(len(nums)):
            if nums[front] != 0 and nums[back] == 0:
                nums[front], nums[back] = nums[back], nums[front]
            if nums[back] != 0:
                back += 1

        return nums
        


        