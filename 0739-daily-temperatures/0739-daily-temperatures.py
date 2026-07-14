class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        l = 0
        res = [0]*n
        for r in range(n):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = r - prev
            stack.append(r)
        return res