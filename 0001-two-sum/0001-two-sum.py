class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictionary = {}
        for i in range(n):
            dictionary[nums[i]] = i
        for i in range(n):
            temp = target - nums[i]
            if (temp in dictionary and dictionary[temp] != i):
                return [i,dictionary[temp]]
        return []