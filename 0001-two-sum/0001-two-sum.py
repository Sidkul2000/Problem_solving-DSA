class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in mp:
                return[i, mp[temp]]
            mp[num] = i

