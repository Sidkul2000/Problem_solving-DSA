class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?,.';":
            paragraph = paragraph.replace(c, " ")
        mp = {}
        count = 0
        res = ""

        for w in paragraph.lower().split():
            if w in banned:
                continue
            elif w in mp:
                mp[w] += 1
            else:
                mp[w] = 1
            if mp[w] > count:
                count = mp[w]
                res = w
        return res