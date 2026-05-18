from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxstr = 0
        substr = deque()
        for i in s:
            while i in substr:
                substr.popleft()
            substr.append(i)
            maxstr = max(maxstr, len(substr))

        return maxstr
                
            