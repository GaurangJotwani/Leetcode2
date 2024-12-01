class Solution:
    
    def find(self, i, parents):
        if parents[i] == i:
            return i
        parents[i] = self.find(parents[i], parents)
        return parents[i]

    def union(self, i, j, parents, ranks):

        par1 = self.find(i, parents)
        par2 = self.find(j, parents)

        if par1 == par2:
            return False
        if ranks[par1] > ranks[par2]:
            ranks[par1] += ranks[par2]
            parents[par2] = par1
        else:
            ranks[par2] += ranks[par1]
            parents[par1] = par2
        
        return True

    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        ranks = [1] * n
        parents = [i for i in range(n)]

        for i,j in edges:
            if self.union(i, j, parents, ranks):
                n -= 1
        
        return n
