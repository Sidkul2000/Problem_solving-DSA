class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        ans = []
        negative = (numerator < 0) ^ (denominator < 0)
        if negative:
            ans.append("-")
        n = abs(numerator)
        d = abs(denominator)

        ans.append(str(n//d))
        ans.append(".")

        rem = n % d
        seen = {}
        idx = 0

        while rem != 0:
            if rem in seen:
                idx = seen[rem]
                ans.insert(idx, "(")
                ans.append(")")
                return "".join(ans)
            seen[rem] = len(ans)
            rem *= 10
            ans.append(str(rem // d))
            rem %= d
        return "".join(ans)



        