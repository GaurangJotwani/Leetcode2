class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {(len(s1), len(s2)): True}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            k = i + j
            if j < len(s2) and s3[k] == s2[j]:
                cache[(i, j)] = dfs(i, j + 1)
                if cache[(i, j)]:
                    return True
            if i < len(s1) and s3[k] == s1[i]:
                cache[(i, j)] = dfs(i + 1, j)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)
                
        
        
        
        