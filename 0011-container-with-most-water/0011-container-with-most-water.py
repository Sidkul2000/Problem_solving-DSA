class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        if n == 2:
            return min(height[0], height[1])
        if n == 1:
            return 0
        l = 0
        r = n-1
        while(l<r):
            w = min(height[l], height[r])*(r-l)
            water = max(water, w)
            if height[l] <= height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return water



