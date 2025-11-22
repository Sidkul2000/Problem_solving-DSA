class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        arr = []
        n = len(potions)

        for spell in spells:
            index = self.bs(spell, potions, success)
            if index == -1:
                arr.append(0)
            else:
                arr.append(n - index)
        return arr

    def bs(self, spell, potions, success):
        l = 0
        r = len(potions) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2
            if potions[m] * spell >= success:
                index = m
                r = m - 1
            else:
                l = m + 1
        return index
