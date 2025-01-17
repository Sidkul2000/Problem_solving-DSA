class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        rows = Counter(tuple(r) for r in grid)
        for i in zip(*grid):
            c += rows[tuple(i)]
        return c



