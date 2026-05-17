class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        while row < m:
            if matrix[row][0] <= target <= matrix[row][n - 1]:
                break
            row += 1

        if row == m:
            return False

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False