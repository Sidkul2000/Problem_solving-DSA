import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mp = {}
        res = []
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for key,v in mp.items():
            heapq.heappush(heap, (v,key))
            if len(heap) > k:
                heapq.heappop(heap)

        for v,key in heap:
            res.append(key)
        return res
