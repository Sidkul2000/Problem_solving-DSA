class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        ans = 0
        mod = 1000000007
        for i in s:
            if i == "1":
                c += 1
            else:
                c = 0
            ans = (ans + c) % mod
        return ans

        