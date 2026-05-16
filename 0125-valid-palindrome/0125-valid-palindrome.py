import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]','',s)
        clean_s = clean_s.lower()
        flag = False
        if clean_s == "" or len(clean_s)==1:
            return True
        l, r = 0, len(clean_s)-1
        while l<r:
            if clean_s[l]==clean_s[r]:
                l+=1
                r-=1
                flag = True
            else:
                return False
        return flag