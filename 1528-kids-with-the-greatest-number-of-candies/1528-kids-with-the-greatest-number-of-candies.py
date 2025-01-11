class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxim = max(candies)
        result = []
        n = len(candies)
        for i in range(n):
            # candies[i] = candies[i] + extraCandies
            if (candies[i] + extraCandies) >= maxim:
                # maxim = candies[i]
                result.append(True)
            else:
                result.append(False)

        return result
                    