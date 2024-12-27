class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []
        def dfs(cNum):
            if cNum > n:
                return
            
            res.append(cNum)
            cNum *= 10
            for i in range(10):
                dfs(cNum + i)
        
        for i in range(1,10):
            dfs(i)
        
        return res


            



