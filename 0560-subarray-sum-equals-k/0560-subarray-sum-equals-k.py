class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        d = {}
        for n in nums:
            s += n

            if s == k:
                count += 1

            if (s-k) in d:
                count += d[s-k]
                
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return count

        