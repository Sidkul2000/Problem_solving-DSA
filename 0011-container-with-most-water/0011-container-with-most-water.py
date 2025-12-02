class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        n = len(height)
        left, right = 0, n-1
        maxwater = min(height[0], height[n-1]) * (n-1)
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > maxwater:
                maxwater = water
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxwater

