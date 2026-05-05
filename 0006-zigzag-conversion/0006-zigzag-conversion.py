class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        l = 0
        matrix = [[] for _ in range(numRows)]
        while l < n:
            for i in range(numRows):
                if l<n:
                    matrix[i].append(s[l])
                    l += 1
            for j in range(numRows-2, 0, -1):
                if l<n:
                    matrix[j].append(s[l])
                    l += 1
        answer = ""
        for i in matrix:
            answer += ''.join(i)
        return answer


