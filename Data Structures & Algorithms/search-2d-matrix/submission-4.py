class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix[0])
        l,r = 0, len(matrix[0]) * len(matrix) - 1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid//x][mid%x] == target:
                return True
            elif matrix[mid//x][mid%x] < target:
                l = mid +1
            else:
                r = mid-1
        return False