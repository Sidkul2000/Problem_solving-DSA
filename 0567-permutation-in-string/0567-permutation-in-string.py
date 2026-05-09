class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=1
        n1 = len(s1)
        n2 = len(s2)
        r = n1
        if n1 > n2:
            return False
        mp1, mp2 = Counter(s1), Counter(s2[0:n1])
        # mp1 = {}
        # mp2 = {}
        # for i in s1:
        #     if i in mp1:
        #         mp1[i] += 1
        #     mp1[i] = 1
        # for i in s2[0:n1]:
        #     if i in mp2:
        #         mp2[i] += 1
        #     mp2[i] = 1
        if mp1 == mp2:
            return True
        while r<n2:
            mp2[s2[l-1]] -= 1
            mp2[s2[r]] += 1
            if mp1 == mp2:
                return True
            r += 1
            l += 1
        return False
            
                
        
        