class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mp = defaultdict(str)
        
        for i in moves:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        if mp["U"]==mp["D"] and mp["L"]==mp["R"]:
            return True
        else:
            return False
        