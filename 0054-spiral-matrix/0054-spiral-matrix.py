class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1


        while row_start <= row_end and col_start <= col_end:

            for c in range(col_start, col_end + 1):
                res.append(matrix[row_start][c])
            
            for r in range(row_start + 1, row_end + 1):
                res.append(matrix[r][col_end])
            
            if row_start != row_end:
                for c in range(col_end - 1, col_start - 1, -1):
                    res.append(matrix[row_end][c])
            
            if col_end != col_start:
                for r in range(row_end - 1, row_start, -1):
                    res.append(matrix[r][col_start])
            
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        
        return res

