class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        numRows -= 1
        if numRows == 0: return [[1]]
        if numRows == 1: return [[1], [1,1]]

        res = [[1], [1,1]]

        for i in range(2, numRows + 1):
            temp = [1]
            for j in range(i - 1):
                temp.append(res[i - 1][j] + res[i - 1][j+1])
            temp.append(1)
            res.append(temp)
        

        return res

        