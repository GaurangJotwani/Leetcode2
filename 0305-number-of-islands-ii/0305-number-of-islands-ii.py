class UnionFind:
    def __init__(self, m, n):
        self.parent = {}
        self.rank = {}
    
    def add(self, r, c):
        if (r, c) not in self.parent:
            self.parent[(r, c)] = (r, c)
            self.rank[(r, c)] = 0
    
    def find(self, r, c):
        if self.parent[(r, c)] != (r, c):
            self.parent[(r, c)] = self.find(*self.parent[(r, c)])  # Path compression
        return self.parent[(r, c)]
    
    def union(self, r1, c1, r2, c2):
        root1 = self.find(r1, c1)
        root2 = self.find(r2, c2)
        
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        uf = UnionFind(m, n)
        visited = set()
        num_islands = 0
        result = []
        
        for r, c in positions:
            if (r, c) in visited:
                result.append(num_islands)
                continue
            
            uf.add(r, c)
            visited.add((r, c))
            num_islands += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    if uf.union(r, c, nr, nc):
                        num_islands -= 1
            
            result.append(num_islands)
        
        return result
