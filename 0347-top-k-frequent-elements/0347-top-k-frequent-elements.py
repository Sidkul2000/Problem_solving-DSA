class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        heap = []
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for key, val in mp.items():
            heapq.heappush(heap, (-val, key))
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])

        return ans
            
        