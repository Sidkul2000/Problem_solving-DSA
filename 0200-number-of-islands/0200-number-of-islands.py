from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        islands = 0
        d = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            # queue = deque()
            # queue.append((r,c))
            # seen.add((i,j))
            # while queue:
            #     ro, co = queue.popleft()
            #     for dr, dc in d:
            #         row = ro+dr
            #         col = co+dc
            #         if row in range(m) and col in range(n) and (row,col) not in seen and grid[row][col]=="1":
            #             seen.add((row,col))
            #             queue.append((row,col))
            seen.add((r,c))
            for dr, dc in d:
                ro, co = r+dr, c+dc
                if ro in range(m) and co in range(n) and (ro,co) not in seen and grid[ro][co]=="1":
                    dfs(ro,co)




        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in seen:
                    islands += 1
                    dfs(i,j)
        return islands