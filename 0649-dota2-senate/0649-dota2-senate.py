class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = [i for i in range(n) if senate[i] == 'R']
        dire = [j for j in range(n) if senate[j] == 'D']
        while rad and dire:
            r = rad.pop(0)
            d = dire.pop(0)
            if r < d:
                rad.append(n+r)
            else:
                dire.append(n+d)
        if rad:
            return "Radiant"
        else:
            return "Dire"


        