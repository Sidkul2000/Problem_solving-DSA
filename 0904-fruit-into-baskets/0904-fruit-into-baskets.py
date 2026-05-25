class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            mp[fruits[r]] += 1
            while len(mp)>2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        return res

            
        