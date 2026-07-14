from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxstr = 0
        seen = deque()
        for r in s:
            while r in seen:
                seen.popleft()
            seen.append(r)
            maxstr = max(maxstr, len(seen))
        return maxstr

