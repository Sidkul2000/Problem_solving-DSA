class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        sol = 0
        while (front < back):
            area = (back - front) * min(height[front], height[back])
            sol = max(sol, area)
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        return sol
            

