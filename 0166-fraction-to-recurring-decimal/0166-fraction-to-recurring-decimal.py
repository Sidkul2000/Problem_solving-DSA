class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator % denominator)==0:
            return str(numerator//denominator)
        negative = (numerator < 0) ^ (denominator < 0)
        num, den = abs(numerator), abs(denominator)

        integer = num//den
        result = "-" if negative else ""
        result += str(integer) + "."

        rem = num%den
        mp = {}
        decimal = []

        while rem != 0:
            if rem in mp:
                repeat = mp[rem]
                decimal.insert(repeat, "(")
                decimal.append(")")
                break
            
            mp[rem] = len(decimal)
            rem *= 10
            digit = rem//den
            decimal.append(str(digit))
            rem %= den
        
        return result + "".join(decimal)
            