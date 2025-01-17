class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0] * (n + 1)
        for i in range(n):
            alt[i+1] = alt[i] + gain[i]
        maxim = max(alt)
        return maxim