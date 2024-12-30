
class UnionFind:

    def __init__(self, m, n):
        self.ranks = [[1] * n for _ in range(m)]
        self.parents = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                self.parents[r][c] = (r, c)

    def find(self, r, c):
        if self.parents[r][c] == (r, c):
            return (r,c)
        tmp = self.find(self.parents[r][c][0],self.parents[r][c][1])
        self.parents[r][c] = tmp
        return tmp

    def union(self, r1, c1, r2, c2):

        p1 = self.find(r1,c1)
        p2 = self.find(r2,c2)
       
        if p1 == p2:
            return False
        
        r1, c1 = p1
        r2, c2 = p2
        
        if self.ranks[r1][c1] > self.ranks[r2][c2]:
            self.parents[r2][c2] = self.parents[r1][c1]
            self.ranks[r1][c1] += self.ranks[r2][c2]
        else:
            self.parents[r1][c1] = self.parents[r2][c2]
            self.ranks[r2][c2] += self.ranks[r1][c1]
        
        return True
        
        
        
    



class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        union_find = UnionFind(m, n)

        number_of_components = 0
        answer = []

        for r,c in positions:

            if (r,c) in visited:
                answer.append(number_of_components)
                continue

            nearby_islands = set()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < m and 0 <= col < n and (row, col) in visited:
                    nearby_islands.add(union_find.find(row, col))
            
            number_of_components += 1
            number_of_components -= len(nearby_islands)
            for r1, c1 in nearby_islands:
                union_find.union(r1, c1, r, c)
            visited.add((r, c))
            answer.append(number_of_components)
        return answer

        