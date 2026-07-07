class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        res = []
        for n in nums:
            if n in mp:
                mp[n] += 1
            else:
                mp[n] = 1
        for k,v in mp.items():
            if v > len(nums)//3:
                res.append(k)
        return res