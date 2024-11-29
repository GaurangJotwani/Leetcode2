class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:


        counts = defaultdict(int)
        res = 0
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            row = matrix[i]
            if row[0] == 1:
                for c in range(n):
                    row[c] = 0 if row[c] == 1 else 1
            row = [chr(bit) for bit in row]
            key = "".join(row)
            counts[key] += 1
            res = max(res, counts[key])
        
        return res