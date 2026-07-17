class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in s:
            if i-1 not in s:
                curr = i
                streak = 1
                while curr+1 in s:
                    curr += 1
                    streak += 1
                res = max(res, streak)
        return res

