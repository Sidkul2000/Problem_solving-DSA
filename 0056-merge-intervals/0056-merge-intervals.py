class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        res = []
        intervals.sort()
        prev = intervals[0]
        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(i[1],prev[1])
            else:
                res.append(prev)
                prev = i
        res.append(prev)
        return res
        