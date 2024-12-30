class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        

        matrix = [[0] * n for _ in range(n)]
        i = 1


        s_r, s_c, e_r, e_c = 0, 0, n - 1, n - 1


        while s_r <= e_r and s_c <= e_c:

            for c in range(s_c, e_c + 1):
                matrix[s_r][c] = i
                i += 1
            for r in range(s_r + 1, e_r + 1):
                matrix[r][e_c] = i
                i += 1
            for c in range(e_c -1, s_c - 1, -1):
                matrix[e_r][c] = i
                i += 1
            for r in range(e_r - 1, s_r, -1):
                matrix[r][s_c] = i
                i += 1
            
            s_r += 1
            e_r -= 1
            s_c += 1
            e_c -= 1


        return matrix