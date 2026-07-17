from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        minutes = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in d:
                    ro = r+dr
                    co = c+dc
                    if ro in range(m) and co in range(n) and grid[ro][co]==1:
                        grid[ro][co] = 2
                        fresh -= 1
                        queue.append((ro,co))
            minutes += 1
        return minutes if fresh==0 else -1