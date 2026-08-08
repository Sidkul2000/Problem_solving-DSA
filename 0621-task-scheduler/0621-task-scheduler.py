import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        time = 0

        queue = deque()

        while queue or max_heap:
            time += 1
            if max_heap:
                c = 1 + heapq.heappop(max_heap)
                if c:
                    queue.append([c,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
