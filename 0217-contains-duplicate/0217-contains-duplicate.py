class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            num.append(nums[i])
        return False
        