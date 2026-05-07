import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        heap = []
        li = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key in freq:
            heapq.heappush(heap, (freq[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in heap:
            li.append(i[1])
        return li
