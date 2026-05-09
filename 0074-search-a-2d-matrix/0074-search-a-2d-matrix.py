class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        l, r = 0, m-1
        c, mid = 0, 0
        while matrix[c][r] < target and c<n-1:
            c += 1
        
        while l<=r:
            mid = (l+r)//2
            if matrix[c][mid] == target:
                return True
            elif matrix[c][mid] < target:
                l = mid+1
            else:
                r = mid-1
        return False


        