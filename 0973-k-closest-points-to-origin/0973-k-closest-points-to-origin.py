import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []
        for x,y in points:
            s = (x**2 + y**2)
            h.append([s,x,y])
        # print(h)
        heapq.heapify(h)
        while k>0:
            s,x,y = heapq.heappop(h)
            res.append([x,y])
            k-=1
        return res


        