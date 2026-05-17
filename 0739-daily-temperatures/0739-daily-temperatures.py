class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = [] # [temp, idx]
        l, r = 0, 1
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st, si = stack.pop()
                answer[si] = (i-si)
            stack.append([t,i])
        return answer