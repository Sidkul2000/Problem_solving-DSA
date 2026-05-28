class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        water = 0
        if n==1:
            return 0
        while l<r:
            h = min(height[l], height[r])
            water = max(water, h*(r-l))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return water
