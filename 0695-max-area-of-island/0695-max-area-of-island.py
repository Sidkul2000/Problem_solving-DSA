from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        visit = set()

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            area = 1
            while queue:
                row, col = queue.popleft()
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr, dc in directions:
                    ro = row + dr
                    co = col + dc
                    if (ro in range(m) and co in range(n) and grid[ro][co]==1 and (ro,co) not in visit):
                        area += 1
                        visit.add((ro,co))
                        queue.append((ro,co))
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1 and (r,c) not in visit:
                    a = bfs(r,c)
                    maxArea = max(maxArea, a)
        return maxArea