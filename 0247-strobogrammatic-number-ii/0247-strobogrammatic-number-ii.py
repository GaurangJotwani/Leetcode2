class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        res = []
        def dfs(root):
            if len(root) > n:
                return
            if len(root) == n:
                if root[0] == "0" and n > 1:
                    return 
                res.append(root)
                return
            dfs("0" + root + "0")
            dfs("1" + root + "1")
            dfs("8" + root + "8")
            dfs("6" + root + "9")
            dfs("9" + root + "6")
        
        if n % 2 == 1:
            dfs("0")
            dfs("1")
            dfs("8")
        else:
            dfs("00")
            dfs("11")
            dfs("88")
            dfs("69")
            dfs("96")
        res.sort()
        return res