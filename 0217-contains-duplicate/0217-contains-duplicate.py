class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # mp = {}
        # for i in nums:
        #     if i in mp:
        #         return True
        #     mp[i] = 1
        # return False
        n = set(nums)
        return len(nums)!=len(n)