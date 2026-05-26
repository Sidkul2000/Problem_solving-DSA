from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                row, col = queue.popleft()
                for dr, dc in directions:
                    ro,co = row+dr, col+dc
                    if (ro in range(m) and co in range(n) and grid[ro][co]=="1" and (ro,co) not in visit):
                        visit.add((ro,co))
                        queue.append((ro,co))


        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    bfs(r,c)
        return islands