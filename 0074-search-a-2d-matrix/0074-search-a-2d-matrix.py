class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        r, c = 0, len(matrix[0]) - 1
        
        
        while r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0]):
            
            c_val = matrix[r][c]
            
            if target == c_val:
                return True
            if target < c_val:
                c -= 1
            else:
                r += 1
        