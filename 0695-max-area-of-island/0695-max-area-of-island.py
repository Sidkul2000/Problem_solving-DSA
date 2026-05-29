from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        maxa = 0

        def bfs(r,c):
            seen.add((r,c))

            q = deque()
            q.append((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    ro = row+dr
                    co = col+dc
                    if ro in range(m) and co in range(n) and grid[ro][co]==1 and (ro,co) not in seen:
                        area += 1
                        seen.add((ro,co))
                        q.append((ro,co))
            return area
                


        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    area = bfs(i,j)
                    maxa = max(maxa, area)
        return maxa
