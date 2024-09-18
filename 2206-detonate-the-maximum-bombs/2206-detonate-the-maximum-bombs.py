class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adjList = defaultdict(list)

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):  # Include the case where j < i as well
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dist_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if dist_squared <= r1 ** 2:  # Compare against the radius squared
                    adjList[i].append(j)
        
        visited = set()
        def dfs(node):
            visited.add((node))
            ans = 1
            for nei in adjList[node]:
                if nei not in visited:
                    ans += dfs(nei)
            
            return ans
        
        res = 0
        for i in range(len(bombs)):
            visited = set()
            res = max(res, dfs(i))
        
        return res


        
        

        