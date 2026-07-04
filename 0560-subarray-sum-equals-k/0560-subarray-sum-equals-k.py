class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        count = 0
        s = 0

        for n in nums:
            s += n
            if s==k:
                count += 1
            
            if (s-k) in mp:
                count += mp[s-k]

            if s in mp:
                mp[s] += 1
            else:
                mp[s] = 1
        return count