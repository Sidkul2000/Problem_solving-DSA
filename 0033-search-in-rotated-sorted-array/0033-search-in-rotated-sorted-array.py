class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if nums[l] <= nums[m] < nums[r]:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m+1
                else:
                    return m
            else:
                if target < nums[l]:
                    l = m+1
                elif target > nums[r]:
                    r = m-1
                else:
                    return m
        return -1