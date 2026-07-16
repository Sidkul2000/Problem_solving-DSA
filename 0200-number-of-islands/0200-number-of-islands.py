from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        islands = 0
        d = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(r,c):
            seen.add((r,c))
            queue = deque()
            queue.append((r,c))
            while queue:
                ro, co = queue.popleft()
                for dr, dc in d:
                    row = ro + dr
                    col = co + dc
                    if row in range(m) and col in range(n) and grid[row][col]=="1" and (row,col) not in seen:
                        seen.add((row,col))
                        queue.append((row,col))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    islands += 1
                    dfs(i,j)
        return islands
