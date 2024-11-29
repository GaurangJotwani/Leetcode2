class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows > len(s):
            return s
        factor = 2 * (numRows - 2) + 2

        res = []

        for r in range(numRows):
            res.append(s[r])
            if r == 0 or r == numRows - 1:
                for i in range(r + factor,len(s),factor):
                    res.append(s[i])
            else:
                i = r
                rows_below = numRows - r - 1
                while i < len(s):
                    if i + rows_below * 2 < len(s):
                        res.append(s[i + rows_below * 2])
                    if i + factor < len(s):
                        res.append(s[i + factor])
                    i += factor

        return "".join(res)
            

        