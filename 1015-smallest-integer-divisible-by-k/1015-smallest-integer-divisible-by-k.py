class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        if k == 1:
            return 1
        rem = 0
        i = 1
        while (i <= k):
            rem = (rem*10 + 1) % k
            if rem == 0:
                return i
            i += 1
        return -1