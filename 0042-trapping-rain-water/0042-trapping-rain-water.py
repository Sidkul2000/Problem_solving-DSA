class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl, maxr = height[0], height[n-1]
        res = 0
        l, r = 0, n-1
        while l<r:
            if maxl <= maxr:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]
        return res

