class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def satisfy(d1, d2, c1, c2, mid):
            notdiv1 = mid - mid//d1
            notdiv2 = mid - mid//d2
            notdivboth = mid - mid//(lcm(d1,d2))
            if notdiv1 >= c1 and notdiv2 >= c2 and notdivboth >= (c1+c2):
                return True
            else:
                return False
        
        l = 0
        h = 10**10
        ans = 10**10
        while (l <= h):
            mid = (l + h)//2
            if satisfy(divisor1, divisor2, uniqueCnt1, uniqueCnt2, mid):
                ans = min(ans, mid)
                h = mid - 1
            else:
                l = mid + 1

        return ans

        
            
            
        