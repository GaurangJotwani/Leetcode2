class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for c in range(len(matrix[0])):
            if not self.isDiagToep(matrix, c, 0):
                return False
        
        for r in range(len(matrix)):
            if not self.isDiagToep(matrix, 0, r):
                return False
        
        return True
    

    def isDiagToep(self, matrix, c, r):
        val = matrix[r][c]

        while r < len(matrix) and c < len(matrix[0]):
            if matrix[r][c] != val:
                return False
            r += 1
            c += 1
        return True