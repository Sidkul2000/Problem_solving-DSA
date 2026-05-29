class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, t, s = 0, 0, 0
        for i in range(n):
            total = total + gas[i] - cost[i]
            t = t + gas[i] - cost[i]
            if t<0:
                t=0
                s = i+1
        if total < 0:
            return -1
        else:
            return s