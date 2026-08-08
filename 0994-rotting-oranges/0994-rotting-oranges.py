from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = deque()
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            minutes += 1
            for l in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in d:
                    r = row+dr
                    c = col+dc
                    if r in range(m) and c in range(n) and grid[r][c]==1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r,c))
        
        return minutes if fresh==0 else -1
        

