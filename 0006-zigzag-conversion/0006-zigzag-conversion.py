class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        l = 1
        if len(s) == 1 or numRows == 1:
            return s
        word = [""] * numRows
        for w in s:
            word[i] += w
            if i == 0:
                l = 1
            elif i == numRows-1:
                l = -1
            i += l
        
        return ''.join(word)
            


        