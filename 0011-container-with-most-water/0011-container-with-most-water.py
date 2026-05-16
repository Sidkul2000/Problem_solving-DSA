class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = 0
        l, r = 0, len(height)-1
        while l<=r:
            w = min(height[l],height[r]) * (r-l)
            maxw = max(w, maxw)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxw

        