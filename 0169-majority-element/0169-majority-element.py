class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # mp = {}
        # for n in nums:
        #     if n in mp:
        #         mp[n] += 1
        #     else:
        #         mp[n] = 1
        # for num, n in mp.items():
        #     if n > len(nums)//2:
        #         return num

        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate