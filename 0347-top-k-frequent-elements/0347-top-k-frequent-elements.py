import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        heap = []
        res = []

        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for key, val in mp.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        for key, val in heap:
            res.append(val)
        return res